from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)  # rows, cols

while True:
    print(I2C_ADDR)
    lcd.blink_cursor_on()
    lcd.putstr(f"I2C Address: {I2C_ADDR}\n")
    lcd.putstr("Shadow Garden")
    sleep(2)
