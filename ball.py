from constants import constant as c
class ball:
	def __init__(self):
		self.x=0
		self.y=0
		self.yDir=1
		self.xDir=1
		self.serves=0

	def checkHit(self, paddle1Y, paddle2Y):
		if self.xDir == -1 and self.x==0 and paddle1Y > self.y and (paddle1Y-c.BAT_HIEGHT) < self.y:
			return True
		if self.xDir == 1 and self.x==c.WINDOW_WIDTH-1 and paddle2Y > self.y and (paddle2Y-c.BAT_HIEGHT) < self.y:
			return True
		else:
			return False

	def checkHitSide(self):
		if self.yDir==1 and self.y>c.WINDOW_HEIGHT:
			return True
		if self.yDir==-1 and self.y<0:
			return True
		else:
			return False

	def checkScore(self):
		if self.xDir == -1 and self.x < 0:
			return -1 #scored on left side (right gains point)
		if self.xDir == 1 and self.x == c.WINDOW_WIDTH:
			return 1 #scored on the right side (left gains point)
		else:
			return 0 #no score
	
	def ballPos(self):
		return (self.x, self,y)
