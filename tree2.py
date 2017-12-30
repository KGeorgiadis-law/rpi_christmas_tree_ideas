#!/usr/bin/python3

from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep
tree = LEDBoard(*range(2,28),pwm=True)
while True:
    for led in tree:
     led.on()
     p = raw_input('please press enter...')
     led.off()
pause()
