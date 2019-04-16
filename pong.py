import pygame, sys
from pygame.locals import *

#Number of frames per second
FPS = 200
#size of the window
WINDOW_WIDTH  = 400
WINDOW_HIEGHT = 200

def main():
	pygame.init()
	#creates a global surface for pygame to draw on
	global DISPLAYSURF
	#allows to specify how fast the program runs
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOWHEIGHT))
	pygame.display.set_caption("Pong")

	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pyagame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == "__main__":
	main()
