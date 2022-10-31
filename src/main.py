import utime
from machine import ADC, Pin

# ADC: https://pico-adc.markomo.me/

# https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/

# adc_pin = Pin(28 Pin.IN)  # ADC2
analog_value = ADC(28)

while True:
    reading = analog_value.read_u16()
    print(' ' * 16, end='\r')
    print(f"ADC: {reading}", end='\r')
    utime.sleep(0.2)
