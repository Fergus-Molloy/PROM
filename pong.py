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
	write(chr(27)+"[0;0H")
	for y in range(c.WINDOW_HEIGHT):
		row = chr(27)+ "[%d;0H" %(y,)
		write(row)
		for x in range(c.WINDOW_WIDTH):
			write(chr(27)+"[40m ")
	write(chr(27)+"[0;0H")

def drawInit():
	clear()
	color = chr(27) + "[44m "
	for x in range(c.BAT_SIZE):
		batHeight = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2 + x
		bat1 = "[%d;0H" %(batHeight,)
		bat2 = "[%d;%dH" %(batHeight, c.WINDOW_WIDTH)
		write(chr(27)+bat1)
		write(chr(27)+color)
		write(chr(27)+bat2)
		write(chr(27)+color)

	color1 = "[40m "
	color2 = "[42m "
	for x in range(c.WINDOW_HEIGHT):
		middle = "[%d;%dH" %(x, c.WINDOW_WIDTH/2)
		write(chr(27)+middle)
		if x%4 == 0:
			write(chr(27)+color1)
		else:
			write(chr(27)+color2)

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
