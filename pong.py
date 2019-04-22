#import RPi.GPIO as GPIO
import readchar
import time, sys
#from serial import Serial
from constants import constant as c

def write(string):
	sys.stdout.write(str(string))

def serialSetup():
	serialPort = Serial("/dev/ttyAMA0", 9600)
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
	for x in range(batY,c.BAT_SIZE):
		bat = "[%d;0H" %(x,)
		write(c.esc+bat)
		write(c.colorBlue)

def drawRightBat(batY):
	write(c.esc+"[0;0H")
	for x in range(c.BAT_SIZE):
		batHeight = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2 + x
		bat = "[%d;%dH" %(x, c.WINDOW_WIDTH)
		write(c.esc+bat)
		write(c.colorBlue)

def drawBats(pos)
	drawLeftBat(pos)
	drawRightBat(pos)

#-----Draw Center-----
def drawCenter():
	for x in range(c.WINDOW_HEIGHT):
		middle = "[%d;%dH" %(x, c.WINDOW_WIDTH/2)
		write(c.esc+middle)
		if x%4 == 0:
			write(c.esc+color1)
		else:
			write(c.esc+color2)

#-----Draw Initial-----
def drawInit():
	clear()
	middle = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2
	drawBats(middle)


#----------Main----------
def main():
#	serailPort = serialSetup()

	drawInit()
	go = True
	while go:
#		inputString = serialPort.read()
		inputString = readchar.readchar()
		if ord(inputString) == 112:
			go = False
			clear()


if __name__ == "__main__":
	main()
