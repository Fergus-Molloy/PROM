import smbus
import time


class I2C:
    def __init__(self):
        self.I2C_ADDR = 0x38
        self.ledValues = [0x7f, 0xbf, 0xdf, 0xef, 0xf7, 0xfb, 0xfd, 0xfe]
        self.bus = smbus.SMBus(1)
        self.bus.write_byte(self.I2C_ADDR, 0xff)

    def update_leds(self, number):
        if number < 0 or number > 7:
            raise Exception("number must be between 1 and 8")
        self.bus.write_byte(self.I2C_ADDR, self.ledValues[number])
