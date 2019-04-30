import RPi.GPIO as GPIO
import time, sys
from ball import ball
from paddle import paddle
from serial import Serial
from constants import constant as c

#gloabal variables needed
global b, leftScore, rightScore, paddleLeft, paddleRight
b = ball()
leftScore=0
rightScore=0
paddleLeft  = paddle("left")
paddleRight = paddle("right")

def write(string):
#	sys.stdout.write(str(string))
	serialPort.write(str(string))

def serialSetup():
	global serialPort
	serialPort = Serial("/dev/ttyAMA0", 115200)
	if serialPort.isOpen() == False:
		serialPort.open()
	return serialPort

def clear():
	write(c.esc+"[0;0H")
	for y in range(c.WINDOW_HEIGHT):
		row = c.esc+ "[%d;0H" %(y,)
		write(row)
		for x in range(c.WINDOW_WIDTH):
			write(c.colorBlack)
	write(c.esc+"[0;0H")

#-----Draw Bats-----
def drawLeftBat(batY):
	write(c.esc+"[0;0H")
	for y in range(batY, batY+c.BAT_SIZE):
		bat = "[%d;0H" %(y,)
		write(c.esc+bat)
		write(c.colorBlue)

def drawRightBat(batY):
	write(c.esc+"[0;0H")
	for x in range(batY, batY+c.BAT_SIZE):
		bat = "[%d;%dH" %(x, c.WINDOW_WIDTH)
		write(c.esc+bat)
		write(c.colorBlue)

def drawBats(pos):
	drawLeftBat(pos)
	drawRightBat(pos)

#-----Draw Center-----
def drawCenter():
	b=1 #for 2 bit counter starting at 1 makes it pretty
	middle = "[0;%dH" %(c.WINDOW_WIDTH/2,)
	write(c.esc+middle)
	for x in range(c.WINDOW_HEIGHT):
		if b == 3: #2 bits are full
			b = 0 #"overflow"
			write(c.colorYellow)
		elif b < 2:
			b += 1
			write(c.colorBlack)
		else:
			b += 1
			write(c.colorYellow)
		write(c.esc+"[1B")
		write(c.esc+"[1D")

#-----Draw Scores-----
def scoreSequence(score):
	scores =[
	c.zero,
	c.one,
	c.two,
	c.three,
	c.four,
	c.five,
	c.six,
	c.seven,
	c.eight,
	c.nine
	]
	return scores[score]

def drawLeftScore(leftScore):
	xOffset = c.WINDOW_WIDTH / 4
	yOffset = c.WINDOW_HEIGHT / 10
	string = scoreSequence(leftScore)
	write(chr(27)+"[%d;%dH"%(yOffset,xOffset))
	for x in string:
		write(x)

def drawRightScore(rightScore):
	xOffset =c.WINDOW_WIDTH - (c.WINDOW_WIDTH/4)
        yOffset = c.WINDOW_HEIGHT / 10
        string = scoreSequence(rightScore)
        write(chr(27)+"[%d;%dH"%(yOffset,xOffset))
        for x in string:
                write(x)

def drawScores():
	drawLeftScore(leftScore)
	drawRightScore(rightScore)
	write(c.esc+"[40m ")
	write(c.esc+"[0;0H")
	string = c.esc + "[%s;%sH"%(b.y, b.x)
	write(string)

#------Draw Ball-----
def drawBall():
	write(c.esc+"[1D"+c.colorBlack)
	string = c.esc + "[%s;%sH"%(b.y, b.x)
	write(string)
	write(c.colorWhite)
def clearBall():
	string  = c.esc+"[%s;%sH"%(b.y, b.x)
	write(string)
	write(c.colorBlack)

def updateBall():
		clearBall()
                if b.yDir>0:
                        b.y+=1
                elif b.yDir<0:
                        b.y-=1

                if b.xDir>0:
                        b.x+=1
                elif b.xDir<0:
                        b.x-=1

                if b.checkHit(paddleLeft.y, paddleRight.y):
                        b.xDir *= -1
                if b.checkHitSide():
                        b.yDir *= -1
		score = b.checkScore()
                if score == 1:
			global leftScore
			leftScore = leftScore + 1
			drawLeftScore(leftScore)
                        #b.serve()
                elif score == -1:
			global rightScore
                        rightScore += 1
			drawRightScore(rightScore)
                        #b.serve()
#                return b.ballPos()

def ballOnCenter():
	if b.x == c.WINDOW_WIDTH/2:
		return True
	else:
		return False

def ballOnScore():
	leftXOffset = c.WINDOW_WIDTH / 4
	rightXOffset = c.WINDOW_WIDTH - leftXOffset
	yOffset = c.WINDOW_HEIGHT / 10
	if b.x > leftXOffset-1 and b.x < leftXOffset+3 and \
	b.y > yOffset-1 and b.y < yOffset+5:
		return True
	elif b.x > rightXOffset-1 and b.x < rightXOffset+3 and \
	b.y > yOffset-1 and b.y < yOffset+5:
		return True
	else:
		return False

#-----Draw Initial-----
def drawInit():
	clear()
	middle = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2
	drawBats(middle)
	drawCenter()
	drawScores()
	drawBall()
#	drawArea()
#	write(c.esc+"[0;0H")

def drawArea():
	leftXOffset = c.WINDOW_WIDTH / 4
	rightXOffset = c.WINDOW_WIDTH - leftXOffset
	yOffset  = (c.WINDOW_HEIGHT / 10)
	for x in range(c.WINDOW_WIDTH):
		for y in range(c.WINDOW_HEIGHT):
			write(c.esc+"[%s;%sH"%(y,x))
			if x > leftXOffset-1 and x < leftXOffset+3:
				print "x: %s" %(True,)
				if y > yOffset-1 and y < yOffset+5:
					print "y: %s" %(True,)
					write(c.colorCyan)
			elif x > rightXOffset-1 and x < rightXOffset+3:
				print "x: %s" %(True,)
				if y > yOffset-1 and y < yOffset+5:
					print "y: %s" %(True,)
					write(c.colorCyan)
			#else:
			#	write(c.colorBlack)

#-----GPIO-----
def initGPIO():
	exclude  = [1,2,4,6,9,14,17,20,25,30,31,34,39]
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	for x in range(1,40):
		if not x in exclude:
			GPIO.setup(x, GPIO.OUT)
			print x
			GPIO.output(x, True)
			time.sleep(10)
			GPIO.output(x, False)

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
			time.sleep(0.05)
			continue
		elif redrawScore:
			updateBall()
			drawScores()
			redrawScore = False
			time.sleep(0.05)
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
		time.sleep(0.05)
#		if not gameStart:
#		inputString = serialPort.read()
#		inputString = readchar.readchar()
#		if ord(inputString) == 112:
#			go = False
#			clear()


if __name__ == "__main__":
	main()
