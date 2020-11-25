import fileinput
import psutil

def applyOverclock(obj, newFreq, newOvervolt):
	# Check to see if "arm_freq" or "over_voltage" already exists
	with open("/boot/config.txt", "r") as bootConfigFile:
		for num, line in enumerate(bootConfigFile, 0):
			if "arm_freq=" in line:
				existingArmFreq = line
				replaceOverclock(newFreq, existingArmFreq)
			elif "over_voltage=" in line:
				existingOvervolt = line
				replaceOvervolt(newOvervolt, existingOvervolt)
	if "existingArmFreq" not in locals():
		with open("/boot/config.txt", "a") as bootConfigFile:
			bootConfigFile.write("arm_freq=" + str(newFreq) + "\n")
	if "existingOvervolt" not in locals():
		with open("/boot/config.txt", "a") as bootConfigFile:
			bootConfigFile.write("over_voltage=" + str(newOvervolt) + "\n")



def replaceOverclock(newFreq, existingArmFreq):
	with fileinput.FileInput("/boot/config.txt", inplace=1, backup=".bak") as bootConfigFile:
			for line in bootConfigFile:
				if line == existingArmFreq:
					print(line.replace(existingArmFreq, "arm_freq=" + str(newFreq)))
				if line != existingArmFreq:
					print(line, end="")
			fileinput.close()

def replaceOvervolt(newOvervolt, existingOvervolt):
	with fileinput.FileInput("/boot/config.txt", inplace=1, backup=".bak") as bootConfigFile:
			for line in bootConfigFile:
				if line == existingOvervolt:
					print(line.replace(existingOvervolt, "over_voltage=" + str(newOvervolt)))
				if line != existingOvervolt:
					print(line, end="")
			fileinput.close()