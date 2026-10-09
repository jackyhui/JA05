# Step 2 - ESP32 blinks ONE LED.
#
# Wiring: no change from Step 1.
#   GPIO16 -- [220 ohm] -- LED long leg (+)
#   LED short leg (-) -- GND
#
# Stop the program with Ctrl+C.

from machine import Pin
import time

led = Pin(16, Pin.OUT)

while True:
    led.value(1)       # ON
    time.sleep(0.5)    # wait 0.5 s
    led.value(0)       # OFF
    time.sleep(0.5)

# Try it: change 0.5 to 0.1. What happens?
