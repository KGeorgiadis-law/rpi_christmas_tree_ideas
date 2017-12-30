#!/usr/bin/python3

from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep
tree = LEDBoard(*range(2,28),pwm=True)
tree[0].pulse(1.5, 1)

rows = [
      [12, 8, 5, 19],
      [4, 13, 20, 18, 22, 10],
      [6, 16, 2, 7, 11, 15, 3, 24],
      [11, 23, 14, 9],
      [17]
       ]


while True:
    for row in rows: # light up each row in succession
     for i in row: # pulse all lights in row
      led = tree[i]
      led.source_delay = 0.1
      led.pulse()

     sleep(0.4) # sleep for half a second

    sleep(1)

    rows.reverse()

    for row in rows: # turn off all lights except for 0 (the star)
     for i in row:
      led = tree[i]
      led.off()

     sleep(0.4)

    sleep(1)

    rows.reverse()
