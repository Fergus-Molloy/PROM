class ball:
	x=0
	y=0
	yDir=1
	xDir=1

	def updateBall(self):
		if yDir>0:
			y+=1
		elif yDir<0:
			y-=1

		if xDir>0:
			x+=1
		elif xDir<0:
			x-=1

		checkHit()
		checkScore()
		drawBall()
