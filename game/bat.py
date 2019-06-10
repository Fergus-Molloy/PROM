import draw
from constants import constant as c

class bat:
    def __init__(self, side):
        if side == "left":
            self.x = 0
        elif side == "right":
            self.x = c.WINDOW_WIDTH-1
        else:
            raise Exception("side should be left or right")
        self.y = c.WINDOW_HEIGHT/2

    def setY(self, y): #prevents bat going off screen
        if y < 0:
            self.y = 0
        elif y > c.WINDOW_HEIGHT-3:
            self.y = c.WINDOW_HEIGHT-3
        else:
            self.y = y
