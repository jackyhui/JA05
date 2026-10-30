# Step 0b - Test every part on its own, before you trust any of them.
#
# WHAT YOU DO: run it. Answer three questions with your eyes.
#
# Wiring: the full Lesson 6 circuit.
#   Sound sensor: V -> 3V3, G -> GND, S -> SENSOR VP
#   LEDs:         GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#
# This file does not measure anything. It asks three questions, one at a
# time, and you answer each one with your eyes. If a part fails here, you
# know exactly which wire to look at. You never have to guess.
#
# Stop the program with Ctrl+C.

from machine import ADC, Pin
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

mic = ADC(Pin(36))
mic.atten(ADC.ATTN_11DB)
mic.width(ADC.WIDTH_12BIT)

print("TEST 1 of 3: the LEDs, one at a time.")
print("You should see 5 LEDs light up left to right.")
for i in range(5):
    leds[i].value(1)
    print("  LED on GPIO", PINS[i])
    time.sleep(0.6)
    leds[i].value(0)
print("Did all 5 light? If one stayed dark, that LED or its resistor is the problem.")
print()

print("TEST 2 of 3: the sound sensor, in silence.")
print("Say nothing for 3 seconds.")
time.sleep(1)
quiet = [mic.read() for i in range(50)]
print("  lowest:", min(quiet), " highest:", max(quiet), " gap:", max(quiet) - min(quiet))
print("A gap under about 60 is a healthy quiet room.")
print("A gap of 0 every time means S is not on SENSOR VP.")
print("A gap of hundreds in silence means the screw is turned too far.")
print("Turn it the other way a little and run this test again.")
print()

print("TEST 3 of 3: the sound sensor, with noise.")
print("Clap your hands now, and keep clapping.")
time.sleep(1)
noisy = [mic.read() for i in range(200)]
print("  lowest:", min(noisy), " highest:", max(noisy), " gap:", max(noisy) - min(noisy))
print("The gap should be clearly bigger than in TEST 2.")
print("Same gap as TEST 2? Check the S wire, then turn the gain screw")
print("clockwise a little and run this test again.")
print()
print("All three passed? Then any bug from here on is in YOUR CODE, not the wiring.")
