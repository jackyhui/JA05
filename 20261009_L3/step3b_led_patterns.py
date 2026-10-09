# Step 3b - Make patterns with 5 LEDs.
#
# Wiring: no change from Step 3a.
#   GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#
# Stop the program with Ctrl+C.

from machine import Pin
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]


def show(pattern):
    # pattern is a list of 5 numbers, 1 = ON, 0 = OFF. Example: [1, 0, 1, 0, 1]
    for led, state in zip(leds, pattern):
        led.value(state)


def chase():
    # One light runs from LED 1 to LED 5
    for i in range(5):
        pattern = [0, 0, 0, 0, 0]
        pattern[i] = 1
        show(pattern)
        time.sleep(0.15)


def bar(count):
    # Light the first "count" LEDs. bar(3) -> [1, 1, 1, 0, 0]
    show([1 if i < count else 0 for i in range(5)])


try:
    while True:
        chase()
        chase()

        for count in range(6):   # bar grows: 0, 1, 2, 3, 4, 5 LEDs
            bar(count)
            time.sleep(0.3)

        show([1, 0, 1, 0, 1])
        time.sleep(0.5)
        show([0, 1, 0, 1, 0])
        time.sleep(0.5)

        # Try it: add your own pattern here with show([...])
finally:
    show([0, 0, 0, 0, 0])        # all off when you press Ctrl+C
