import RPi.GPIO as GPIO				
import time
import sys

class ldr():
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
        time.sleep(0.001)
        GPIO.output(self.RESET_PIN, False) 

        while GPIO.input(self.TEST_PIN) == 0:
            self.count +=1	
        return self.count 

    def getCount( self ):
        return self.count

class button():
  def__init__(self, pin1,pin2):
    self.BUTTON_1 = pin1
    self.BUTTON_2 = pin2
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(self.BUTTON_1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(self.BUTTON_2, GPIO.IN,pull_up_down=GPIO.PUD_UP)

` def update(self,pin):
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
  
def main():
    print("main program")
    ldr1 = ldr( 10, 9 )
    buttons1 = (11, 15)
    while True: 
        countA = ldr1.update()
        outputString = "Resistor value = " + str(countA) 
        print outputString
        buttonval = buttons1.update()
        outputString2 = "Button 1 Value = " + buttonval[0]
        outputString3= "Button 2 Value = " + buttonval[1]
        print outputString2
        print outputString3
        time.sleep(0.5) 
        sys.stdout.write("\033[2A")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
