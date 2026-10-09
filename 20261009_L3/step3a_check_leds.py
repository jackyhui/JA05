# Step 3a - Check each of the 5 LEDs, one at a time.
#
# Wiring: copy the Step 1 circuit 5 times.
#   LED 1: GPIO16 -- [220 ohm] -- LED -- GND
#   LED 2: GPIO17 -- [220 ohm] -- LED -- GND
#   LED 3: GPIO18 -- [220 ohm] -- LED -- GND
#   LED 4: GPIO19 -- [220 ohm] -- LED -- GND
#   LED 5: GPIO23 -- [220 ohm] -- LED -- GND
#
# Each LED lights for 1 second and the Shell tells you which one it is.
# If an LED does not light when its name is printed, check THAT LED only:
#   1. Is the long leg on the resistor side?
#   2. Is the short leg connected to GND?
#   3. Is the wire in the right GPIO pin?

from machine import Pin
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

for led in leds:
    led.value(0)

for number, led in enumerate(leds, 1):
    print("LED", number, "on GPIO", PINS[number - 1], "-> ON")
    led.value(1)
    time.sleep(1)
    led.value(0)

print("Done. Did all 5 LEDs light up?")
