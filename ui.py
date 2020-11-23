# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon/assets/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.overview = QtWidgets.QWidget()
        self.overview.setObjectName("overview")
        self.formLayoutWidget = QtWidgets.QWidget(self.overview)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.platformHeader = QtWidgets.QLabel(self.formLayoutWidget)
        self.platformHeader.setObjectName("platformHeader")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.platformHeader)
        self.platformData = QtWidgets.QLabel(self.formLayoutWidget)
        self.platformData.setObjectName("platformData")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.platformData)
        self.firmwareHeader = QtWidgets.QLabel(self.formLayoutWidget)
        self.firmwareHeader.setObjectName("firmwareHeader")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firmwareHeader)
        self.firmwareData = QtWidgets.QLabel(self.formLayoutWidget)
        self.firmwareData.setObjectName("firmwareData")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firmwareData)
        self.architectureHeader = QtWidgets.QLabel(self.formLayoutWidget)
        self.architectureHeader.setObjectName("architectureHeader")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.architectureHeader)
        self.architectureData = QtWidgets.QLabel(self.formLayoutWidget)
        self.architectureData.setObjectName("architectureData")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.architectureData)
        self.hostnameHeader = QtWidgets.QLabel(self.formLayoutWidget)
        self.hostnameHeader.setObjectName("hostnameHeader")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.hostnameHeader)
        self.hostnameData = QtWidgets.QLabel(self.formLayoutWidget)
        self.hostnameData.setObjectName("hostnameData")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hostnameData)
        self.tabWidget.addTab(self.overview, "")
        self.fan_control = QtWidgets.QWidget()
        self.fan_control.setObjectName("fan_control")
        self.fanAnimate = QtWidgets.QLabel(self.fan_control)
        self.fanAnimate.setGeometry(QtCore.QRect(0, 0, 98, 98))
        self.fanAnimate.setPixmap(QtGui.QPixmap("icons/fan.gif"))
        self.fanAnimate.setObjectName("fanAnimate")
        self.toolBox = QtWidgets.QToolBox(self.fan_control)
        self.toolBox.setGeometry(QtCore.QRect(100, 0, 291, 171))
        self.toolBox.setObjectName("toolBox")
        self.fanmode = QtWidgets.QWidget()
        self.fanmode.setGeometry(QtCore.QRect(0, 0, 291, 60))
        self.fanmode.setObjectName("fanmode")
        self.fanModeActiveButton = QtWidgets.QRadioButton(self.fanmode)
        self.fanModeActiveButton.setGeometry(QtCore.QRect(10, 0, 117, 28))
        self.fanModeActiveButton.setChecked(False)
        self.fanModeActiveButton.setObjectName("fanModeActiveButton")
        self.fanModePassiveButton = QtWidgets.QRadioButton(self.fanmode)
        self.fanModePassiveButton.setGeometry(QtCore.QRect(130, 0, 117, 28))
        self.fanModePassiveButton.setChecked(True)
        self.fanModePassiveButton.setObjectName("fanModePassiveButton")
        self.fanModeLabel = QtWidgets.QLabel(self.fanmode)
        self.fanModeLabel.setGeometry(QtCore.QRect(10, 30, 271, 23))
        self.fanModeLabel.setWordWrap(True)
        self.fanModeLabel.setObjectName("fanModeLabel")
        self.toolBox.addItem(self.fanmode, "")
        self.gpiosetup = QtWidgets.QWidget()
        self.gpiosetup.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.gpiosetup.setObjectName("gpiosetup")
        self.fanGPIOBox = QtWidgets.QSpinBox(self.gpiosetup)
        self.fanGPIOBox.setGeometry(QtCore.QRect(10, 20, 50, 21))
        self.fanGPIOBox.setMaximum(40)
        self.fanGPIOBox.setProperty("value", 19)
        self.fanGPIOBox.setObjectName("fanGPIOBox")
        self.fanGPIOLabel = QtWidgets.QLabel(self.gpiosetup)
        self.fanGPIOLabel.setGeometry(QtCore.QRect(70, 10, 211, 41))
        self.fanGPIOLabel.setWordWrap(True)
        self.fanGPIOLabel.setObjectName("fanGPIOLabel")
        self.toolBox.addItem(self.gpiosetup, "")
        self.temperaturethreshold = QtWidgets.QWidget()
        self.temperaturethreshold.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.temperaturethreshold.setObjectName("temperaturethreshold")
        self.tempThresholdBox = QtWidgets.QSpinBox(self.temperaturethreshold)
        self.tempThresholdBox.setGeometry(QtCore.QRect(0, 20, 50, 21))
        self.tempThresholdBox.setMaximum(100)
        self.tempThresholdBox.setProperty("value", 70)
        self.tempThresholdBox.setObjectName("tempThresholdBox")
        self.tempLabel = QtWidgets.QLabel(self.temperaturethreshold)
        self.tempLabel.setGeometry(QtCore.QRect(60, 10, 221, 41))
        self.tempLabel.setWordWrap(True)
        self.tempLabel.setObjectName("tempLabel")
        self.toolBox.addItem(self.temperaturethreshold, "")
        self.fanControlApply = QtWidgets.QPushButton(self.fan_control)
        self.fanControlApply.setGeometry(QtCore.QRect(300, 230, 96, 29))
        self.fanControlApply.setFlat(False)
        self.fanControlApply.setObjectName("fanControlApply")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.fan_control)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 210, 291, 52))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.currentTempHeader = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.currentTempHeader.setObjectName("currentTempHeader")
        self.verticalLayout.addWidget(self.currentTempHeader)
        self.currentTempData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.currentTempData.setObjectName("currentTempData")
        self.verticalLayout.addWidget(self.currentTempData)
        self.tabWidget.addTab(self.fan_control, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.label = QtWidgets.QLabel(self.about)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 261))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.about, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Raspi Control Panel"))
        self.tabWidget.setToolTip(_translate("Form", "<html><head/><body><p>Raspberry Pi Configuration</p></body></html>"))
        self.platformHeader.setText(_translate("Form", "Platform:"))
        self.platformData.setText(_translate("Form", "Loading..."))
        self.firmwareHeader.setText(_translate("Form", "Firmware:"))
        self.firmwareData.setText(_translate("Form", "Loading..."))
        self.architectureHeader.setText(_translate("Form", "Architecture:"))
        self.architectureData.setText(_translate("Form", "Loading..."))
        self.hostnameHeader.setText(_translate("Form", "Hostname:"))
        self.hostnameData.setText(_translate("Form", "Loading..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overview), _translate("Form", "Overview"))
        self.fanAnimate.setText(_translate("Form", "<html><head/><body><p><img src=\":/fan_animate/assets/fan.gif\"/></p></body></html>"))
        self.fanModeActiveButton.setText(_translate("Form", "Active"))
        self.fanModePassiveButton.setText(_translate("Form", "Passive"))
        self.fanModeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Enables or disables fan control</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.fanmode), _translate("Form", "Fan Mode"))
        self.fanGPIOLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">GPIO fan pin - recommended to set this value to 19</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.gpiosetup), _translate("Form", "GPIO Setup"))
        self.tempLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Temperature at which the fan should turn on, in Celsius.</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.temperaturethreshold), _translate("Form", "Temperature Threshold"))
        self.fanControlApply.setText(_translate("Form", "Apply"))
        self.currentTempHeader.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Current Temperature (</span><span style=\" font-family:\'DDG_ProximaNova,DDG_ProximaNova_UI_0,DDG_ProximaNova_UI_1,DDG_ProximaNova_UI_2,DDG_ProximaNova_UI_3,DDG_ProximaNova_UI_4,DDG_ProximaNova_UI_5,DDG_ProximaNova_UI_6,Proxima Nova,Helvetica Neue,Helvetica,Segoe UI,Nimbus Sans L,Liberation Sans,Open Sans,FreeSans,Arial,sans-serif\'; font-size:11pt; color:#222222; background-color:#ffffff;\">°C):</span></p></body></html>"))
        self.currentTempData.setText(_translate("Form", "Loading..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fan_control), _translate("Form", "Fan Control"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Raspi Control Panel</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Written by AnonymousHacker1279</span></p><p align=\"center\"><a href=\"https://titan-mk4.dynv6.net\"><span style=\" font-weight:600; color:#000000;text-decoration:none;\">A basic tool to control specific features on your Raspberry Pi. Designed from the ground up in Python and PyQt5.</span></a></p><p align=\"center\"><a href=\"https://github.com/AnonymousHacker1279\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a><a href=\"https://github.com/AnonymousHacker1279\"><span style=\" text-decoration: underline; color:#000000;\">, </span></a><a href=\"https://titan-mk4.dynv6.net\"><span style=\" text-decoration: underline; color:#0000ff;\">My Website</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("Form", "About"))

import resource_rc
