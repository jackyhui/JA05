# Step 3 - The classroom noise meter.
#
# WHAT YOU DO: write TWO lines, inside the loop. Marked YOUR CODE.
#
# Wiring:
#   Sound sensor: V -> 3V3, G -> GND, S -> SENSOR VP
#   LEDs:         GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#
# The meter must count loud MOMENTS, not loud readings. One long shout is
# one moment, not forty. So the program has to remember two things between
# one round of the loop and the next:
#
#   loud_count   how many loud moments so far
#   was_loud     was the room loud LAST time round?
#
# Both are made before the loop. If you make them inside the loop, the
# program forgets everything every round, and the count never grows.
#
# Stop the program with Ctrl+C.

from machine import ADC, Pin
import time

# ===== 1. SETUP: the pins and the sensor =====
PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

mic = ADC(Pin(36))
mic.atten(ADC.ATTN_11DB)
mic.width(ADC.WIDTH_12BIT)


# ===== 2. NUMBERS YOU CAN CHANGE =====
SAMPLES = 50
QUIET = 60
LOUD = 1200
TOO_LOUD_LEVEL = 4       # level 4 or 5 counts as too loud
COOLDOWN = 2.0           # seconds of quiet before a new moment can be counted



# ===== 3. FUNCTIONS: the thinking =====
def loudness():
    lowest = 4095
    highest = 0
    for i in range(SAMPLES):
        value = mic.read()
        if value < lowest:
            lowest = value
        if value > highest:
            highest = value
    return highest - lowest


def level_for(gap):
    """0 to 5, same shape as Step 1."""
    if gap <= QUIET:
        return 0
    if gap >= LOUD:
        return 5
    return 1 + int((gap - QUIET) * 4 / (LOUD - QUIET))


def show(level):
    for i in range(5):
        leds[i].value(1 if i < level else 0)



# ===== 4. THE MEMORY: made once, before the loop =====
# The program's memory. Made ONCE, before the loop.
loud_count = 0
was_loud = False
last_count_time = 0


# ===== 5. THE LOOP: again and again, until you stop it =====
try:
    while True:
        gap = loudness()
        level = level_for(gap)
        show(level)

        is_loud = level >= TOO_LOUD_LEVEL
        now = time.time()

        # >>>>> YOUR CODE STARTS HERE >>>>>
        # Line 1: count a new loud moment. Only if the room
        # was quiet before, and only if COOLDOWN seconds
        # passed since the last one. Add 1 to loud_count,
        # then set last_count_time = now.
        if False:
            pass

        # Line 2: remember is_loud for next time round.

        # <<<<< YOUR CODE ENDS HERE <<<<<

        print("gap:", gap, " level:", level, " loud moments:", loud_count)
        time.sleep(0.1)

finally:
    show(0)
    print("Stopped. Loud moments this session:", loud_count)

# Try it: clap once. The count should go up by exactly 1.
# Try it: shout for five seconds. Still 1? Good. Still counting up? Fix the memory.
# Try it: change TOO_LOUD_LEVEL to 3. Does your room trip it too easily?
