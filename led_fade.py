# by Lucas Miller
# code help from harrison and mr h.
# led fade -

import board
import pulseio    # all of these are integers.
import time

led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)    # sets up pin.

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:

            led.duty_cycle = int(i * 2 * 65535 / 100)
            # this fades up, i.e makes the led turn on and get brighter.
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)
            # this fades down, i.e makes the led fade off
        time.sleep(0.025)    # this is the circuit python version of a delay.

    # 66535 is the brightest the LED can be.
    # 0 is the lowest it can be.