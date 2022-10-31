import utime
from machine import Pin


class Pins:
    def __init__(self):
        self.RED = Pin(26, Pin.OUT)
        self.YELLOW = Pin(27, Pin.OUT)
        self.GREEN = Pin(28, Pin.OUT)
        
        self.RED.low()
        self.YELLOW.low()
        self.GREEN.high()

    def green_to_red(self):
        if self.RED.value() == 1:
            return
        
        self.GREEN.high()
        # utime.sleep(5)
        self.GREEN.low()
        self.YELLOW.high()
        utime.sleep(1)

        self.YELLOW.low()
        self.RED.high()
        utime.sleep(5)

    def red_to_green(self):
        if self.GREEN.value() == 1:
            return

        self.YELLOW.high()
        utime.sleep(1)

        self.RED.low()
        self.YELLOW.low()
        self.GREEN.high()
        utime.sleep(5)

    

pins = Pins()



while True:
    pins.green_to_red()
    print("Toggled to red")
    pins.red_to_green()
    print("Toggled to green")
