#!/usr/bin/python3

# inspired from http://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#who-s-home-indicator

from gpiozero import LEDBoard, PingServer
from gpiozero.tools import random_values
from signal import pause
from time import sleep
import timeout_decorator
from timeout_decorator.timeout_decorator import TimeoutError

tree = LEDBoard(*range(2,28),pwm=True)

##### 
# CHANGE THESE
#####

family_members = {
      '192.168.xx.xx': [[5, 19, 8, 21, 12], 'gremlin'], 
      '192.168.xx.xx': [[18, 22, 10, 4, 13, 20], 'vampire'],
      '192.168.xx.xx': [[11, 24, 3, 6, 16, 2, 7], 'santa'],
      '192.168.xx.xx': [[9, 25, 15, 23, 14], 'wolverine'],
      '192.168.xx.xx': [[17], 'IT'],
      }

@timeout_decorator.timeout(1)
def PingServerTimeout(ip):
    return PingServer(ip).value

while True:
    family = list()
    for ip, row in family_members.items():
     try:
      person = PingServerTimeout(ip)
     except TimeoutError:
      person = False
     if person:
      family.append(person)
      for i in row[0]: # pulse all lights in row
       led = tree[i]
       led.pulse()
     else:
      for i in row[0]:
       led = tree[i]
       led.off()

    if len(family) != 0:
     tree[0].pulse(1 / len(family))
    else:
     tree[0].off()
    sleep(1)