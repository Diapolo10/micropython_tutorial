import utime
from machine import Pin

led = Pin(28, Pin.OUT)
led.low()

while True:
    led.toggle()
    print("Toggle")
    utime.sleep(1)
