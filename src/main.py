import _thread
import utime
from machine import Pin


class TrafficLight:
    def __init__(self):
        self.RED = Pin(26, Pin.OUT)
        self.YELLOW = Pin(27, Pin.OUT)
        self.GREEN = Pin(28, Pin.OUT)
        self.BUTTON = Pin(22, Pin.IN, Pin.PULL_DOWN)

        self.button_pressed = False

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

    def red_to_green(self):
        if self.GREEN.value() == 1:
            return

        self.YELLOW.high()
        utime.sleep(1)

        self.RED.low()
        self.YELLOW.low()
        self.GREEN.high()

    def blinking_yellow(self):
        self.RED.low()
        self.YELLOW.low()
        self.GREEN.low()

        utime.sleep(1)

        self.YELLOW.high()


def button_reader_thread(traffic_light):
    while True:
        if traffic_light.BUTTON.value() == 1:
            traffic_light.button_pressed = True
        utime.sleep(0.01)

traffic_light = TrafficLight()

_thread.start_new_thread(button_reader_thread, (traffic_light,))


while True:
    if traffic_light.button_pressed:
        traffic_light.blinking_yellow()
        utime.sleep(1)
        traffic_light.button_pressed = False
    else:
        traffic_light.RED.high()
        utime.sleep(5)
        traffic_light.red_to_green()
        utime.sleep(5)
        traffic_light.green_to_red()
