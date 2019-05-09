import RPi.GPIO as GPIO
import time, sys, draw, I2C, ball, bat, adc
from PyGlow import PyGlow, BOTH
from serial import Serial
from constants import constant as c

#gloabal variables needed
global b, leftScore, rightScore, batLeft, batRight, adc0
adc0 = adc.adc(10,9)
b = ball.ball()
leftScore = 0
rightScore = 0
batLeft  = bat.bat("left")
batRight = bat.bat("right")
speed = 0.04
pg = PyGlow(pulse=True, speed=1000, pulse_dir=BOTH)

def rightScores():
	pg.all(brightness=150)
	pg.all(0)

def write(string):
	serialPort.write(str(string))

def serialSetup():
	global serialPort
	serialPort = Serial("/dev/ttyAMA0", 115200)
	if serialPort.isOpen() == False:
		serialPort.open()
	return serialPort




def updateBall():
		clearBall()
                b.y += b.yDir
                b.x+=b.xDir

                if b.checkHit(batLeft.y, batRight.y):
                        b.xDir *= -1
                if b.checkHitSide():
                        b.yDir *= -1
		score = b.checkScore()
                if score == 1:
			global leftScore
			leftScore = leftScore + 1
			drawLeftScore(leftScore)
			#leftScore()
                        #b.serve()
                elif score == -1:
			global rightScore
                        rightScore += 1
			drawRightScore(rightScore)
			rightScores()
			#b.serve()




#-----GPIO-----
def initGPIO():
	global LEDpins
	LEDpins  = [5,6,12,13,16,19,20,26]
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	for x in LEDpins:
		GPIO.setup(x, GPIO.OUT)
		GPIO.output(x, True)
	time.sleep(1)
	for x in LEDpins:
		GPIO.output(x, False)

def updateLED():
	i2c = I2C()
	ratio = ((float(b.x)/float(c.WINDOW_WIDTH))*7)#index range 0-7
	LED = int(round(ratio))
	for x in LEDpins:
		GPIO.output(x,False)
	GPIO.output(LEDpins[LED], True)
	i2c.updateLEDS(LED)

#-----ADC-----
def updateADC():
	value = adc0.update()
	print "Value: %s" %(value,)
	clear_line()
	batLeft.setY(value)
	drawLeftBat()

#----------Main----------
def main():
	serailPort = serialSetup()
	drawInit()
	go = True
	gameStart = False
	redrawCenter = False
	redrawScore = False
	while go:
		if redrawCenter:
			updateBall()
			drawCenter()
			redrawCenter = False
			time.sleep(speed)
			continue
		elif redrawScore:
			updateBall()
			drawScores()
			redrawScore = False
			time.sleep(speed)
			continue
		else:
			updateBall()

		if ballOnCenter():
			redrawCenter = True
			drawBall()
		elif ballOnScore():
			redrawScore = True
			drawBall()
		else:
			drawBall()
		time.sleep(speed)
		updateLED()
		updateADC()

if __name__ == "__main__":
	main()
