import RPi.GPIO as GPIO
import time, sys
from serial import Serial
from constants import constant as c

def clear(serialPort):
	serialPort.write(chr(27)+"[0;0H")
	for y in range(c.WINDOW_HEIGHT):
#		for x in range(c.WINDOW_WIDTH):
		serialPort.write(chr(27)+"[40m ")
		serialPort.write(chr(27)+"[1B")
		serialPort.write(chr(27)+"[1D")
		print y
	serialPort.write(chr(27)+"[0;0H")

def drawInit(serialPort):
	batHeight = c.WINDOW_HEIGHT/2 - c.BAT_SIZE
	string = "[%d;0H" %(batHeight,)
	serialPort.write(chr(27)+string)
	string = chr(27) + "[44m "
	for x in range(c.BAT_SIZE):
		serialPort.write(string)
		serialPort.write(chr(27)+"[1B")
		serialPort.write(chr(27)+"[1D")

def main():
	serialPort = Serial("/dev/ttyAMA0", 9600)
	
	if serialPort.isOpen() == False:
		serialPort.open()

	drawInit(serialPort)
	go = True
	while go:
		inputString = serialPort.read()
		if ord(inputString) == 112:
			go = False
			clear(serialPort)
			

if __name__ == "__main__":
	main()
