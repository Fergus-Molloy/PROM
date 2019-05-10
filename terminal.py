import RPi.GPIO as GPIO				
import time
import sys
from constants import constant as c

class ldr():
    def __init__( self, pinI, pinO):
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
        time.sleep(0.001)
        GPIO.output(self.RESET_PIN, False) 

        while GPIO.input(self.TEST_PIN) == 0:
            self.count +=1	
        return self.count 

    def getCount( self ):
        return self.count

class button():
    def __init__(self, pin1,pin2):
	self.BUTTON_1 = pin1
	self.BUTTON_2 = pin2
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(self.BUTTON_1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(self.BUTTON_2, GPIO.IN,pull_up_down=GPIO.PUD_UP)

    def update(self):
	b=[0,0]
	while True:
		if (GPIO.input(11)==1):
			b[0]=0
		else:
			b[0]=1
		if (GPIO.input(15)==1):
			b[1]=0
		else:
			b[1]=1
		return b

def getBatSize(batSize):
	return batSize

def main():
    print("main program")
    ldr1 = ldr( 10, 9 )
    buttons = button(11, 15)
    while True: 

        countA = ldr1.update()
	buttonval = buttons.update()
	bat_status = ""
	if getBatSize(c.BAT_SIZE) == 3:
		bat_status = "Normal Size"
	elif getBatSize(c.BAT_SIZE) == 5:
		at_status = "Super Size"
	
        outputString = "Resistor value = " + str(countA)         
        outputString2 = "Button 1 Value = " + str(buttonval[0])
        outputString3= "Button 2 Value = " + str(buttonval[1])
	outputString4 = "Bat Size = " + c.BAT_SIZE
	outputString5 = "Bat Status = " + bat_status
	
	print outputString
        print outputString2
        print outputString3
	print outputString4
	print outputString5

        time.sleep(0.5) 
        sys.stdout.write("\033[3A")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
