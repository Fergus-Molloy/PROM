#Class containing the data for the bat and the scores
import draw
from constants import constant as c


class ball:
    def __init__(self):
        self.x = 2 #infront of bat
        self.y = c.WINDOW_HEIGHT/2
        self.y_dir = 1
        self.x_dir = 1
        self.serves = 0
	self.left_score = 0
	self.right_score = 0
	self.score_counter = 0

    def check_hit(self, left_bat, right_bat):
        if self.x_dir == -1 and self.x+self.x_dir == (left_bat.x):
	    if left_bat.y <= self.y \
	and (left_bat.y+c.BAT_SIZE) > self.y:
		return True
        if self.x_dir == 1 and self.x+self.x_dir == (right_bat.x):
	    if right_bat.y <= self.y \
	and (right_bat.y/2+c.BAT_SIZE) > self.y:
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

    def ball_on_center(self): #for redrawing center line
        if self.x == c.WINDOW_WIDTH/2:
            return True
        else:
            return False

    def ball_pos_3_bit(self):
        ratio = int(round(9*(float(self.x)/100))) #7* because 0 to 7 index
	return ratio

    def ball_on_score(self): #for redrawing score
        left_x_offset = c.WINDOW_WIDTH / 4
        right_x_offset = c.WINDOW_WIDTH - left_x_offset
        y_offset = c.WINDOW_HEIGHT / 10
        if self.x > left_x_offset-1 and self.x < left_x_offset+3 and \
                self.y > y_offset-1 and self.y < y_offset+5:
            return True
        elif self.x > right_x_offset-1 and self.x < right_x_offset+3 and \
                self.y > y_offset-1 and self.y < y_offset+5:
            return True
        else:
            return False

    def update_ball(self, serial_port, left_bat, right_bat):
        draw.clear_ball(serial_port, self)
        self.y += self.y_dir
        self.x += self.x_dir
        if self.check_hit(left_bat, right_bat):
            self.x_dir *= -1
        if self.check_hit_side():
            self.y_dir *= -1
        score = self.check_score()
        if score == 1:
            self.left_score += 1
	    self.score_counter += 1
            draw.draw_left_score(serial_port, self.left_score)
	    #c.SERVE = True
	    #c.SERVE_SIDE = "right"
        elif score == -1:
            self.right_score += 1
	    self.score_counter += 1
            draw.draw_right_score(serial_port, self.right_score)
	    #c.SERVE = True
	    #c.SERVE_SIDE = "left"
