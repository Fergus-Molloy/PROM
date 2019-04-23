import RPi.GPIO as GPIO
#import readchar
import time, sys
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
		bat = "[%d;%dH" %(x, c.WINDOW_WIDTH)
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

def drawScores(score):
	drawLeftScore(score)
	drawRightScore(score)

#-----Draw Initial-----
def drawInit():
	clear()
	middle = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2
	drawBats(middle)
	drawCenter()
	drawScores(9)


#----------Main----------
def main():
	serailPort = serialSetup()

	drawInit()
	go = True
#	while go:
#		inputString = serialPort.read()
#		inputString = readchar.readchar()
#		if ord(inputString) == 112:
#			go = False
#			clear()


if __name__ == "__main__":
	main()
