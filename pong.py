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
	b=1 #for 2 bit counter
	for x in range(c.WINDOW_HEIGHT):
		middle = "[%d;%dH" %(x, c.WINDOW_WIDTH/2)
		write(c.esc+middle)
		if b == 3: #2 bits are full
			b = 0 #"overflow"
			write(c.colorYellow)
		elif b < 2:
			b += 1
			write(c.colorBlack)
		else:
			b += 1
			write(c.colorYellow)

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
	if b.x > leftXOffset and b.x < leftXOffset+3 and \
	b.y < yOffset and b.y > yOffset+5:
		return True
	elif b.x > rightXOffset and b.x < rightXOffset+3 and \
	b.y < yOffset and b.y > yOffset+5:
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
			time.sleep(0.5)
			continue
		elif redrawScore:
			updateBall()
			drawScore()
			time.sleep(0.5)
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
