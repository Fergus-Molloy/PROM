def write(output):
    serialPort.write(str(output))

#-----Clear-----
def clear():
	write(c.esc+"[0;0H")
	for y in range(c.WINDOW_HEIGHT):
		row = c.esc+ "[%d;0H" %(y,)
		write(row)
		for x in range(c.WINDOW_WIDTH):
			write(c.colorBlack)
	write(c.esc+"[0;0H")

def clear_line():
	sys.stdout.write(c.esc+"[1A")
	for x in range(c.WINDOW_WIDTH):
		sys.stdout.write(c.esc+"[40m ")
	sys.stdout.write(c.esc+"[%sD"%(c.WINDOW_WIDTH,))

#-----Draw Bats-----
def drawLeftBat():
	write(c.esc+"[0;0H")
	for y in range(batLeft.y, batLeft.y+c.BAT_SIZE):
		bat = "[%d;%dH" %(y, batLeft.x)
		write(c.esc+bat)
		write(c.colorBlue)

def drawRightBat():
	write(c.esc+"[0;0H")
	for y in range(batRight.y, batRight.y+c.BAT_SIZE):
		bat = "[%d;%dH" %(y, batRight.x)
		write(c.esc+bat)
		write(c.colorBlue)

def drawBats():
	drawLeftBat()
	drawRightBat()

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
	return

def drawRightScore(rightScore):
	xOffset =c.WINDOW_WIDTH - (c.WINDOW_WIDTH/4)
        yOffset = c.WINDOW_HEIGHT / 10
        string = scoreSequence(rightScore)
        write(chr(27)+"[%d;%dH"%(yOffset,xOffset))
        for x in string:
                write(x)
	return

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

#-----Draw Initial-----
def drawInit():
	clear()
	middle = (c.WINDOW_HEIGHT - c.BAT_SIZE)/2
	drawBats()
	drawCenter()
	drawScores()
	drawBall()
	initGPIO()

#-----Debug-----
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