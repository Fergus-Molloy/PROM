import draw
from constants import constant as c

class bat:
    def __init__(self, side):
        if side == "left":
            self.x = 0
        elif side == "right":
            self.x = c.WINDOW_WIDTH
        else:
            raise Exception("side should be left or right")
        self.y = c.WINDOW_HEIGHT/2

    def setY(self, y): #prevents bat going off screen
        if y < 3:
            self.y = 3
        elif y > c.WINDOW_HEIGHT:
            self.y = c.WINDOW_HEIGHT
        else:
            self.y = y
