import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO.input(11)==1):
		print("button status: OFF")
	else:
		print("button status: ON")

	if (GPIO.input(14)==1):
		print("button status: OFF")
	else:
		print("button status: ON")
	time.sleep(0.5)
	sys.stdout.write("\033[1A")
