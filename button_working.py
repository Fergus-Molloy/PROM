import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO.input(11)==1):
		print("button 1 status: 0")
	else:
		print("button 1 status: 1")

	if (GPIO.input(15)==1):
		print("button 2 status: 0")
	else:
		print("button 2 status: 1")
	time.sleep(0.5)
	sys.stdout.write("\033[2A")
