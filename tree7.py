# light up as many rows as there are devices found on the network - do this by pinging the ~10 most common addresses

# inspired from http://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#who-s-home-indicator

from gpiozero import LEDBoard, PingServer
from signal import pause
from time import sleep
import timeout_decorator
from timeout_decorator.timeout_decorator import TimeoutError

tree = LEDBoard(*range(2,28),pwm=True)

@timeout_decorator.timeout(0.5)
def PingServerTimeout(ip):
    return PingServer(ip).value

rows = [[5, 19, 8, 21, 12],
        [18, 22, 10, 4, 13, 20],
        [11, 24, 3, 6, 16, 2, 7],
        [9, 25, 15, 23, 14],
        [17]
       ]

while True:
    devices = list()
    possible_ip_endings = ["11", "30", "23", "26", "22", 
"32", "16", "24", "17", "33"]
    for ip in possible_ip_endings:
        try:
#            print("Pinging 192.168.xx.{}...".format(ip))
            devices.append(PingServerTimeout('192.168.xx.{}'.format(ip)))
        except TimeoutError:
            devices.append(False)

#    print(devices)
    active_devices = [x for x in devices if x == True]
#    print(active_devices)
    number_active_devices = len(active_devices)
#    print(number_active_devices)
    lit_rows = number_active_devices if number_active_devices <= 5 else 5

    lit_rows_list = [x for x in range(lit_rows)]
    total_rows_list = [x for x in range(5)]

    for r in total_rows_list:
        row = rows[r]
        if r in lit_rows_list:
            for l in row:
                led = tree[l]
                led.pulse()
        else:
            for l in row:
                led = tree[l]
                led.off()

    if lit_rows != 0:
        tree[0].pulse(1 / lit_rows)
    else:
        tree[0].off()

    sleep(1)
