import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)
while True:
    GIPO.output(buzzer,GPIO.HIGH)
    print("Beep")
    GPIO.output(buzzer,GPIO.LOW)
    print("no beep")
    sleep(0.5)
