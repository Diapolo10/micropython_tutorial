from machine import I2C, Pin, SoftI2C
from time import sleep
from grove_lcd_i2c import Grove_LCD_I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
# i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=400_000)

I2C_ADDR = i2c.scan()[0]
print(i2c.scan())

lcd = Grove_LCD_I2C(i2c, I2C_ADDR)
lcd.home()

while True:
    print(I2C_ADDR)
    lcd.write(f"I2C Address: {I2C_ADDR}\nShadow Garden")
    sleep(2)
    lcd.clear()
    lcd.home()
    lcd.write(f"I2C Address: {I2C_ADDR:x}\nShadow Garden")
    sleep(2)
    lcd.clear()
