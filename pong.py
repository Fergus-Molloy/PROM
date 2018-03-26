import RPi.GPIO as GPIO
import time, sys
from ball import ball
from paddle import paddle
from serial import Serial
from constants import constant as c

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
		bat = "[%d;%dH" %(x, c.WINDOW_WIDTH-1)
		write(c.esc+bat)
		write(c.colorBlue)

def drawBats(pos):
	drawLeftBat(pos)
	drawRightBat(pos)

#-----Draw Center-----
def drawCenter():
	b=0 #for 2 bit counter
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

def drawLeftScore(score):
	xOffset = c.WINDOW_WIDTH / 4
	yOffset = c.WINDOW_HEIGHT / 10
	string = scoreSequence(score)
	write(chr(27)+"[%d;%dH"%(yOffset,xOffset))
	for x in string:
		write(x)

def drawRightScore(score):
	xOffset =c.WINDOW_WIDTH - (c.WINDOW_WIDTH/4)
        yOffset = c.WINDOW_HEIGHT / 10
        string = scoreSequence(score)
        write(chr(27)+"[%d;%dH"%(yOffset,xOffset))
        for x in string:
                write(x)

def drawScores():
	drawLeftScore(leftScore)
	drawRightScore(rightScore)
	write(c.esc+"[40m ")
	write(c.esc+"[0;0H")

#------Draw Ball-----
def drawBall(ball):
	write(c.colorBlack)
	string = c.esc + "[%s;%sH"%(ball.y, ball.x)
	string += c.colorWhite
	write(string)

def updateBall():
                if b.yDir>0:
                        b.y+=1
                elif b.yDir<0:
                        b.y-=1

                if b.xDir>0:
                        b.x+=1
                elif b.xDir<0:
                        b.x-=1

                if b.checkHit(paddleLeft.y, paddleRight.y):
                        self.xDir *= -1
                if b.checkHitSide():
                        b.yDir *= -1
		score = b.checkScore()
                if score == 1:
			leftScore +=1
			drawLeftScore()
                        #b.serve()
                elif score == -1:
                        rightScore += 1
			drawRightScore()
                        #b.serve()
                return b.ballPos()

#-----Draw Initial-----
def drawInit():
	clear()
	middle = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2
	drawBats(middle)
	drawCenter()
	drawScores()
	drawBall(b)


#----------Main----------
def main():
	serailPort = serialSetup()
	global leftScore, rightScore, paddleLeft, paddleRight, b
	b = ball()
	leftScore=rightScore=0
	paddleLeft  = paddle("left")
	paddleRight = paddle("right")
	drawInit()

	go = True
	gameStart = False
	while go:
		updateBall()
#		if not gameStart:
#		inputString = serialPort.read()
#		inputString = readchar.readchar()
#		if ord(inputString) == 112:
#			go = False
#			clear()


if __name__ == "__main__":
	main()
