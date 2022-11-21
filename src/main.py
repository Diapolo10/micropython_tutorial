import utime
from machine import ADC, I2C, Pin, SoftI2C
from grove_lcd_i2c import Grove_LCD_I2C

analog_value = ADC(28)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
# i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=400_000)

I2C_ADDR = i2c.scan()[0]
print(i2c.scan())

lcd = Grove_LCD_I2C(i2c, I2C_ADDR)
lcd.home()

while True:
    reading = analog_value.read_u16()
    lcd.write(f"I2C Address: {I2C_ADDR}\nADC: {reading:.03f}V")
    utime.sleep(1)
    lcd.clear()
