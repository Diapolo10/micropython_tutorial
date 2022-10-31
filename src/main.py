import utime
from machine import Pin

import DFRobot_ADS1115

# ADC: https://pico-adc.markomo.me/

# https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/

sda_pin = Pin(26, Pin.IN)
clock_pin = Pin(27, Pin.OUT)

while True:
    reading = analog_value.read_u16()
    print(f"{' ' * 16 + '\r'}ADC: {reading}", end='\r')
    utime.sleep(0.2)
