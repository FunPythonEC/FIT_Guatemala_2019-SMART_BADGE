import max7219
from machine import Pin, SPI
import time

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(21), mosi=Pin(16))
ss = Pin(17, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)
display.brightness(15)

text = "fit2019 "
#display.text(text,0,0,1)
#display.show()
while True:
  for i in range(len(text)):
    display = max7219.Matrix8x8(spi, ss, i+1)
    display.text(text,0,0,1)
    time.sleep(1)
    display.show()