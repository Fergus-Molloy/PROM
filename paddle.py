from constants import constant as c

class paddle:
	def __init__(self, side):
		if side == "left":
			self.x = 0
		elif side == "right":
			self.x = c.WINDOW_WIDTH
		else:
			raise Exception("side should be left or right")
		self.y = c.WINDOW_HEIGHT/2
		
	
