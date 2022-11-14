from machine import I2C, Pin, Timer
from time import sleep_ms, ticks_ms, ticks_us
from array import array

import ADS1x15

ADS = ADS1x15.ADS1115(1)
ADS.setMode(ADS.MODE_CONTINUOUS)
ADS.requestADC(0)

# ADC: https://pico-adc.markomo.me/

# https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/

# https://github.com/chandrawi/ADS1x15-ADC

# addr = 72
# gain = 1
# _BUFFERSIZE = const(512)
# ADC_RATE = 5

# data = array("h", (0 for _ in range(_BUFFERSIZE)))
# timestamp = array("L", (0 for _ in range(_BUFFERSIZE)))
# irq_busy = False
# index_put = 0

# sda_pin = Pin(26, Pin.IN)
# clock_pin = Pin(27, Pin.OUT)
# i2c = I2C(1, scl=clock_pin, sda=sda_pin, freq=400_000)
# ads = ADS1115(i2c, addr, gain)


# def sample(x, adc=ads.read_rev, data=data, timestamp=timestamp):
#     global index_put, irq_busy
#     if irq_busy:
#         return
#     irq_busy = True
#     if index_put < _BUFFERSIZE:
#         timestamp[index_put] = ticks_us()
#         data[index_put] = adc()
#         index_put += 1
#     irq_busy = False


# ads.set_conv(7, 0)
# ads.read_rev()
# sleep_ms(ADC_RATE)
# tim = Timer(-1)
# tim.init(period=ADC_RATE, mode=Timer.PERIODIC, callback=sample)

while True:
    reading = ADS.getValue()
    print(' ' * 16, end='\r')
    print(f"ADC: {reading}", end='\r')
    sleep_ms(1000)
