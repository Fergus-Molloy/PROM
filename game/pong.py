import RPi.GPIO as GPIO
import time
import sys
import draw
import I2C
import ball
import bat
import adc
from serial import Serial
from constants import constant as c


def write(serial_port, string):
    serial_port.write(str(string))


def serial_setup():
    serial_port = Serial("/dev/ttyAMA0", 115200)
    if serial_port.isOpen() == False:
        serial_port.open()
    return serial_port


# -----GPIO-----
def init_gpio():
    LEDpins = [5, 6, 12, 13, 16, 19, 20, 26]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for x in LEDpins:
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, True)
    time.sleep(1)
    for x in LEDpins:
        GPIO.output(x, False)


# -----ADC-----
def update_adc(serial_port, adc, left_bat, right_bat):
    value = adc.update() - 9 #adc never outputs less than 9???
    left_bat.setY(c.WINDOW_HEIGHT - value)
    draw.draw_left_bat(serial_port, left_bat)
    draw.draw_right_bat(serial_port, right_bat)
    return left_bat.y + 1

def game_end():
    exit()

def switch_serve(side):
    if side == "left":
	return "right"
    else:
	return "left"

# ----------Main----------
def main():
    serial_port = serial_setup()
    #vairables to controll the game
    ADC = adc.adc(10, 9)
    i2c = I2C.I2C()
    b = ball.ball()
    left_score = 0
    right_score = 0
    left_bat = bat.bat("left")
    right_bat = bat.bat("right")
    speed = 0.00 #1/speed == frequency

    draw.draw_init(serial_port, b, left_bat, right_bat, left_score, right_score)

    redrawCenter = False
    redrawScore = False
    while not c.SERVE:
        if redrawCenter:
            b.update_ball(serial_port, left_bat, right_bat)
            draw.draw_center(serial_port)
            redrawCenter = False
            time.sleep(speed)
            continue
        elif redrawScore:
            b.update_ball(serial_port, left_bat, right_bat)
            draw.draw_scores(serial_port, b, b.left_score, b.right_score)
            redrawScore = False
            time.sleep(speed)
            continue
        else:
            b.update_ball(serial_port, left_bat, right_bat)
	    if b.left_score == 10 or b.right_score == 10:
		game_end()
	    if b.score_counter == 5:
		b.score_counter = 0
		c.SERVE_SIDE = switch_serve(c.SERVE_SIDE)
        if b.ball_on_center():
            redrawCenter = True
            draw.draw_ball(serial_port, b)
        elif b.ball_on_score():
            redrawScore = True
            draw.draw_ball(serial_port, b)
        else:
            draw.draw_ball(serial_port, b)
        time.sleep(speed)
        i2c.update_leds(b.ball_pos_3_bit())
        update_adc(serial_port, ADC, left_bat, right_bat)    
    
    while c.SERVE:
	if c.SERVE_SIDE == "right":
		b.y = right_bat.y
        	b.x == right_bat.x+3
	else:
		b.y = update_adc(serial_port, ADC, left_bat, right_bat)
		b.x == left_bat.x+1
	draw.clear_col(serial_port, b.x)
	draw.draw_ball(serial_port, b)

if __name__ == "__main__":
    main()
