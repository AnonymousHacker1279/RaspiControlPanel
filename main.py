from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import platform
import os
import psutil
from subprocess import Popen, PIPE
import time
import configparser

# Import our files
import fanController
import overclockHandler
import ui
import restartDialog

class RaspiControlPanel(QtWidgets.QWidget, ui.Ui_Form):

	def run(self):
		config = configparser.ConfigParser()
	
		def readConfigurationFile():
			try:
				configFile = open("config.ini")
				configFile.close()
				config.read("config.ini")
			except:
				config['general'] = {}
				config['general']['has_seen_tray_minimize_message'] = 'False'

				config['fanControl'] = {}
				config['fanControl']['is_active'] = 'False'
				config['fanControl']['fan_gpio_setup'] = '19'
				config['fanControl']['fan_temp_threshold'] = '70'

				with open('config.ini', 'w') as configFile:
					config.write(configFile)
					configFile.close()
		readConfigurationFile()

		fanAnimation = QMovie(resource_path('./assets/fan.gif'))
		self.fanAnimate.setMovie(fanAnimation)
		fanAnimation.start()

		platformData = Popen(["cat", "/proc/device-tree/model"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = platformData.communicate()
		stdout = str(stdout)
		stdout = stdout.rstrip("\\x00'")
		stdout = stdout.lstrip("b'")
		self.platformData.setText(str(stdout))

		uname = platform.uname()
		self.firmwareData.setText(uname.release)
		self.architectureData.setText(uname.machine)
		self.hostnameData.setText(uname.node)

		cpufreq = psutil.cpu_freq()
		self.cpuFreqBox.setValue(cpufreq.max)
		with open("/boot/config.txt", "r") as bootConfigFile:
			for num, line in enumerate(bootConfigFile, 0):
				if "over_voltage=" in line:
					line = line.lstrip("over_voltage=")
					line = line.rstrip("\n")
					self.overvoltBox.setValue(int(line))

		def prepareFanValues(obj, didUpdate):
			fanMode = self.fanModeActiveButton.isChecked()
			GPIOSetup = self.fanGPIOBox.value()
			tempThreshold = self.tempThresholdBox.value()

			# Update configuration file
			if didUpdate == True:
				configFile = config.read("config.ini")
				config.set("fanControl", "is_active", str(fanMode))
				config.set("fanControl", "fan_gpio_setup", str(GPIOSetup))
				config.set("fanControl", "fan_temp_threshold", str(tempThreshold))
				with open("config.ini", "w+") as configFile:
					config.write(configFile)
					configFile.close()

			fanController.applyNewFanValues(obj, fanMode, GPIOSetup, tempThreshold)
		self.fanControlApply.clicked.connect(lambda: prepareFanValues(self, True))

		def prepareOverclockValues(obj):
			freqValue = self.cpuFreqBox.value()
			overvoltValue = self.overvoltBox.value()

			overclockHandler.applyOverclock(obj, freqValue, overvoltValue)
			restartDialog = RestartDialog()
			restartDialog.show()
		self.overclockApply.clicked.connect(lambda: prepareOverclockValues(self))


		# If configuration data exists, send the data to any functions that need it
		if "config" in locals():
			if config["fanControl"]:
				fanControl = config["fanControl"]
				fanMode = fanControl["is_active"]
				if fanMode == "True":
					self.fanModeActiveButton.setChecked(True)
				GPIOSetup = int(fanControl["fan_gpio_setup"])
				if GPIOSetup != 19:
					self.fanGPIOBox.setValue(int(fanControl["fan_gpio_setup"]))
				tempThreshold = int(fanControl["fan_temp_threshold"])
				if tempThreshold != 70:
					self.tempThresholdBox.setValue(int(fanControl["fan_temp_threshold"]))
				prepareFanValues(self, False)
			if config["general"]:
				global hasSeenTrayMinimizeMessage
				hasSeenTrayMinimizeMessage = config["general"]["has_seen_tray_minimize_message"]

	def changeEvent(self, event):
		config = configparser.ConfigParser()
		global hasSeenTrayMinimizeMessage
		if event.type() == QEvent.WindowStateChange:
			if self.windowState() & Qt.WindowMinimized:
				self.hide()
				self.tray.show()
				if hasSeenTrayMinimizeMessage == "False":
					self.tray.showMessage("Raspi Control Panel", "The application has minimized to your tray. Right click to show or exit.")
					hasSeenTrayMinimizeMessage = "True"
					configFile = config.read("config.ini")
					config.set("general", "has_seen_tray_minimize_message", "True")
					with open("config.ini", "w+") as configFile:
						config.write(configFile)
						configFile.close()

	def closeEvent(self, event):
		global app
		fanController.exit_handler()
		self.close()
		app.exit()
		
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def __init__(self, parent=None):
		global app
		super(RaspiControlPanel, self).__init__(parent)
		self.setupUi(self)

		icon = QIcon(QtGui.QPixmap(resource_path("./assets/window.png")))
		menu = QMenu()
		showAction = menu.addAction("Show")
		showAction.triggered.connect(lambda: (self.showNormal(),self.tray.hide(),self.setVisible(True)))
		exitAction = menu.addAction("Exit")
		exitAction.triggered.connect(lambda: (fanController.exit_handler(), self.close(), app.exit()))
		self.tray = QSystemTrayIcon()
		self.tray.setIcon(icon)
		self.tray.setContextMenu(menu)
		self.tray.hide()
		self.tray.setToolTip("Raspi Control Panel")

		self.center()
		self.run()

class RestartDialog(QtWidgets.QWidget, restartDialog.Ui_Dialog):
	def __init__(self, parent=None):
		super(RestartDialog, self).__init__(parent)
		self.setupUi(self)
		self.center()
		self.run()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def run(self):
		self.restartLater.clicked.connect(lambda: self.hide())
		self.restartNow.clicked.connect(lambda: os.system("sudo reboot"))

def main():
	global app
	app = QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)
	app.setStyle("Fusion")
	form = RaspiControlPanel()
	form.show()
	app.exec_()

# Translate asset paths to useable format for PyInstaller
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath('.'), relative_path)

if __name__ == '__main__':
	main()