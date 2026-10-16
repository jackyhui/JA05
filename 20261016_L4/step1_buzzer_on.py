# Step 1 - ESP32 turns the buzzer on.
#
# Use the ACTIVE buzzer ("buzzer with power", sealed black back).
#
# Wiring (same as Step 0, but move ONE wire):
#   GPIO25 -- buzzer + (long leg)
#   buzzer - (short leg) -- GND
#
# In Step 0 the + wire went to 3V3. Now move that wire to GPIO25.
# Keep the LEDs and the sensor from Lesson 3 plugged in.

from machine import Pin

buzzer = Pin(25, Pin.OUT)

buzzer.value(1)          # 1 = beep
print("Buzzer should be beeping")

# Try it: change 1 to 0, run again. The buzzer goes quiet.
