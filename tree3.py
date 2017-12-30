#!/usr/bin/python3

from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep
tree = LEDBoard(*range(2,28),pwm=True)
tree[0].pulse(2, 2)
while True:
    for i in range(1, 25):
     led = tree[i]
#     led.source_delay = 0.1
#     led.source = random_values()
     led.pulse()
     sleep(0.3)
    sleep(0.5)
    for i in range(1, 25):
     led = tree[i] 
     led.source = [0]
     sleep(0.1)
    sleep(0.5)
#pause()
