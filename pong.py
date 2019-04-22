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
#		for x in range(c.WINDOW_WIDTH):
		write(chr(27)+"[40m ")
		write(chr(27)+"[1B")
		write(chr(27)+"[1D")
		print y
	write(chr(27)+"[0;0H")

def drawInit():
	batHeight = c.WINDOW_HEIGHT/2 - c.BAT_SIZE
	string = "[%d;0H" %(batHeight,)
	write(chr(27)+string)
	string = chr(27) + "[44m "
	for x in range(c.BAT_SIZE):
		write(string)
		write(chr(27)+"[1B")
		write(chr(27)+"[1D")

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
