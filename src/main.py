import utime
from machine import Pin


class Pins:
    def __init__(self):
        self.RED = Pin(26, Pin.OUT)
        self.YELLOW = Pin(27, Pin.OUT)
        self.GREEN = Pin(28, Pin.OUT)
        self.BUTTON = Pin(15, Pin.IN)

        self.last_time = 0

        self.RED.low()
        self.YELLOW.low()
        self.GREEN.high()

    def read_button_while_waiting_delay_to_end(self, delay):

        self.last_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), self.last_time) < delay:

            utime.sleep(0.04)

            button_value = self.BUTTON.value()
            print(f'button_value: {button_value}')
            if button_value == 1:
                self.RED.low()
                self.YELLOW.low()
                self.GREEN.low()

                utime.sleep(1)

                while True:

                    self.last_time = utime.ticks_ms()
                    while utime.ticks_diff(utime.ticks_ms(), self.last_time) < 1000:

                        utime.sleep(0.04)

                        button_value = self.BUTTON.value()
                        print(f'button_value (sub): {button_value}')
                        if button_value == 1:
                            utime.sleep(1)
                            return

                    if self.YELLOW.value() == 0:
                        self.YELLOW.high()

                    else:
                        self.YELLOW.low()

    def run_lights_cycle(self):
        self.GREEN.low()
        self.YELLOW.high()

        self.read_button_while_waiting_delay_to_end(1000)

        self.YELLOW.low()
        self.RED.high()

        print("Toggled to red")

        self.read_button_while_waiting_delay_to_end(5000)

        self.YELLOW.high()

        self.read_button_while_waiting_delay_to_end(1000)

        self.RED.low()
        self.YELLOW.low()
        self.GREEN.high()

        print("Toggled to green")

        self.read_button_while_waiting_delay_to_end(5000)

        self.RED.low()
        self.YELLOW.low()
        self.GREEN.low()


pins = Pins()


while True:
    pins.run_lights_cycle()
