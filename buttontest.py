GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO(8)==1):
		print("1")
	else:
		print("2")
	time.sleep(1)
