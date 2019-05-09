import RPi.GPIO as GPIO				
import time
import sys
from constants import constant as c

class adc():
    def __init__( self, pinI, pinO  ):
        self.count = 0
        self.RESET_PIN = pinO
        self.TEST_PIN = pinI

        GPIO.setwarnings(False) 	
        GPIO.setmode(GPIO.BCM) 		

        GPIO.setup(self.RESET_PIN, GPIO.OUT) 
        GPIO.output(self.RESET_PIN, False) 	

        GPIO.setup(self.TEST_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update( self ):
        self.count = 0
        GPIO.output(self.RESET_PIN, True) 	
        time.sleep(0.01)
        GPIO.output(self.RESET_PIN, False) 

        while GPIO.input(self.TEST_PIN) == 0:
            self.count +=1	

        return self.count 

    def getCount( self ):
        return self.count

    def clear_line():
		sys.stdout.write(c.esc+"[1A")
		for x in range(c.WINDOW_WIDTH):
			sys.stdout.write(c.esc+"[40m ")
		sys.stdout.write(c.esc+"[%sD"%(c.WINDOW_WIDTH,))
