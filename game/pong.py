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
def update_adc(serial_port, adc, left_bat):
    value = adc.update()
    left_bat.setY(value)
    draw.draw_left_bat(serial_port, left_bat)


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
    speed = 0.04 #1/speed == frequency

    draw.draw_init(serial_port, ball, left_bat, right_bat, left_score, right_score)


    go = True

    redrawCenter = False
    redrawScore = False

    while go:
        if redrawCenter:
            b.update_ball(serial_port, left_bat, right_bat, left_score, right_score)
            draw.draw_center(serial_port)
            redrawCenter = False
            time.sleep(speed)
            continue
        elif redrawScore:
            b.update_ball(serial_port, left_bat, right_bat, left_score, right_score)
            draw.draw_scores(serial_port, ball, left_score, right_score)
            redrawScore = False
            time.sleep(speed)
            continue
        else:
            b.update_ball(serial_port, left_bat, right_bat, left_score, right_score)

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
        update_adc(serial_port, ADC, left_bat)


if __name__ == "__main__":
    main()