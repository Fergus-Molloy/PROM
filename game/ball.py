from constants import constant as c

class ball:
    def __init__(self):
        self.x = 2
        self.y = c.WINDOW_HEIGHT/2
        self.y_dir = 1
        self.x_dir = 1
        self.serves = 0

    def check_hit(self, bat_left, bat_right):
        if self.x_dir == -1 and self.x == 1 and bat_left > self.y and (bat_left-c.BAT_SIZE) < self.y:
            return True
        if self.x_dir == 1 and self.x == (c.WINDOW_WIDTH-1) and bat_right > self.y and (bat_right-c.BAT_SIZE) < self.y:
            return True
        else:
            return False

    def check_hit_side(self):
        if self.y_dir == 1 and self.y > (c.WINDOW_HEIGHT-2):
            return True
        if self.y_dir == -1 and self.y < 2:
            return True
        else:
            return False

    def check_score(self):
        if self.x_dir == -1 and self.x < 1:
            self.x_dir *= -1
            return -1  # scored on left side (right gains point)
        if self.x_dir == 1 and self.x > c.WINDOW_WIDTH-1:
            self.x_dir *= -1
            return 1  # scored on the right side (left gains point)
        else:
            return 0  # no score

    def ballOnCenter():
    	if self.x == c.WINDOW_WIDTH/2:
    		return True
    	else:
			return False

    def ballOnScore():
    leftXOffset = c.WINDOW_WIDTH / 4
    rightXOffset = c.WINDOW_WIDTH - leftXOffset
    yOffset = c.WINDOW_HEIGHT / 10
    if self.x > leftXOffset-1 and self.x < leftXOffset+3 and \
            self.y > yOffset-1 and self.y < yOffset+5:
        return True
    elif self.x > rightXOffset-1 and self.x < rightXOffset+3 and \
            self.y > yOffset-1 and self.y < yOffset+5:
        return True
    else:
        return False

    def update_ball(self, bat_left, bat_right, left_score, right_score):
        draw.clear_ball()
        self.y += self.y_dir
        self.x += self.x_dir
        if self.check_hit(selfat_left.y, selfat_right.y):
            self.x_dir *= -1
        if self.check_hit_side():
            self.y_dir *= -1
        score = self.check_score()
        if score == 1:
            leftScore = leftScore + 1
            drawLeftScore(leftScore)
            # self.serve()
        elif score == -1:
            rightScore += 1
            drawRightScore(rightScore)
            # self.serve()
