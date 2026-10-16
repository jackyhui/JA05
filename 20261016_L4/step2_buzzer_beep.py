# Step 2 - Beep in a rhythm.
#
# Wiring: no change from Step 1.
#   GPIO25 -- buzzer + ,  buzzer - -- GND
#
# Stop the program with Ctrl+C.

from machine import Pin
import time

buzzer = Pin(25, Pin.OUT)

try:
    while True:
        buzzer.value(1)    # beep
        time.sleep(0.05)   # a short beep: 0.05 s
        buzzer.value(0)    # quiet
        time.sleep(0.5)    # wait 0.5 s

        # Try it: change 0.5 to 0.1
finally:
    buzzer.value(0)        # quiet when you press Ctrl+C
