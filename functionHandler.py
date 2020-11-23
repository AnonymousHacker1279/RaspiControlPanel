from PyQt5.QtWidgets import *
import RPi.GPIO as GPIO
import main
import psutil
from threading import Thread
import time
import ui
import atexit

GPIO.setmode(GPIO.BCM)
fanPin = 19
GPIO.setup(fanPin, GPIO.OUT)

global activeMode
global terminate
activeMode = False
terminate = False
tempThreshold = 60
obj = "null"

def driveFan(obj, fanPin, tempThreshold):
	global activeMode
	global terminate
	while activeMode == True:
		if terminate == True:
			break

		temp = psutil.sensors_temperatures()
		temp = temp.get("cpu_thermal")
		temp = temp[0][1]
		if temp >= tempThreshold:
			GPIO.output(fanPin, True)
			obj.currentTempData.setText(str(round(temp, 1)) + "°C  -  Fan ON")
		else:
			GPIO.output(fanPin, False)
			obj.currentTempData.setText(str(round(temp, 1)) + "°C  -  Fan OFF")
		time.sleep(3)
	while activeMode == False:
		if terminate == True:
			break

		temp = psutil.sensors_temperatures()
		temp = temp.get("cpu_thermal")
		temp = temp[0][1]
		GPIO.output(fanPin, False)
		obj.currentTempData.setText(str(round(temp, 1)) + "°C  -  Fan OFF  -  Passive Mode")
		time.sleep(3)

fanThread = Thread(target = driveFan, args = (obj, fanPin, tempThreshold))
def applyNewFanValues(obj, fanMode, GPIOSetup, tempThreshold):
	# Triggers when the Apply button is pressed
	global activeMode
	global terminate
	global fanThread
	global newFanThread
	newFanThread = Thread(target = driveFan, args = (obj, GPIOSetup, tempThreshold))
	if fanMode == True:
		fanPin = GPIOSetup
		GPIO.setup(fanPin, GPIO.OUT)
		activeMode = True
		if fanThread.is_alive() == True:
			terminate = True
			fanThread.join()
			terminate = False
			newFanThread = Thread(target = driveFan, args = (obj, fanPin, tempThreshold))
			newFanThread.start()
			fanThread = newFanThread
		else:
			newFanThread.start()
			fanThread = newFanThread
	else:
		fanPin = GPIOSetup
		GPIO.setup(fanPin, GPIO.OUT)
		activeMode = False
		if fanThread.is_alive() == True:
			terminate = True
			fanThread.join()
			terminate = False
			newFanThread = Thread(target = driveFan, args = (obj, fanPin, tempThreshold))
			newFanThread.start()
			fanThread = newFanThread
		else:
			newFanThread.start()
			fanThread = newFanThread

def exit_handler():
	global terminate
	global fanThread
	terminate = True
	fanThread.join()
	GPIO.output(fanPin, False)

atexit.register(exit_handler)