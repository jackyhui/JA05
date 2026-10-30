# Step 0 - Listen to the room. One reading at a time.
#
# WHAT YOU DO: run it. Change nothing yet.
#
# Wiring (sound sensor module, 3 pins):
#   V -> 3V3        G -> GND        S (analog out) -> SENSOR VP
#
# Use 3V3, not 5V.
#
# SENSOR VP is the third pin down the left-hand side: 3.3V, EN, SENSOR VP.
#
# The blue screw sets how big the signal reaching S is. It is not a
# threshold: your code decides what counts as loud. Set it once and
# leave it, or your numbers stop meaning anything.
#
# On this module the output is clamped: a quiet room sits near 0 and
# sound shows up as spikes upward. That is why the manufacturer's own
# example calls anything over 600 "sound".
#
# Run it, then clap once. Watch the number in the Shell.
#
# Stop the program with Ctrl+C.

from machine import ADC, Pin
import time

mic = ADC(Pin(36))
mic.atten(ADC.ATTN_11DB)      # read the full 0 to 3.3 V
mic.width(ADC.WIDTH_12BIT)    # answer as 0 to 4095

try:
    while True:
        value = mic.read()
        print(value)
        time.sleep(0.2)

finally:
    print("Stopped.")

# Try it: sit still and say nothing for ten seconds. Does the number hold still?
# Try it: clap once. Did you catch the clap, or did the Shell miss it?
# Try it: change 0.2 to 0.02. Now how much does the number jump?
