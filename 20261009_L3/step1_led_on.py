# Step 1 - ESP32 turns ONE LED on.
#
# Wiring (same as Step 0, but move ONE wire):
#   GPIO16 -- [220 ohm] -- LED long leg (+)
#   LED short leg (-) -- GND
#
# In Step 0 the resistor wire went to 3V3. Now move that wire to GPIO16.
# Everything else stays where it is.

from machine import Pin

led = Pin(16, Pin.OUT)   # GPIO16 is an output pin

led.value(1)             # 1 = ON (3.3 V on the pin)
print("LED on GPIO16 should be ON")

# Try it: change 1 to 0, run again. The LED goes OFF.
