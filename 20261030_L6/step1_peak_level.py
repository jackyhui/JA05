# Step 1 - One reading lies. Fifty readings tell the truth.
#
# WHAT YOU DO: write ONE line, inside level_for(). Marked YOUR CODE.
#
# Wiring:
#   Sound sensor: V -> 3V3, G -> GND, S -> GPIO36
#   LEDs:         GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#
# A microphone does not report "how loud". It reports where the
# diaphragm is, right now, thousands of times a second. One reading
# tells you nothing. So we take 50 readings fast, and measure the gap
# between the quietest and the loudest. That gap is the loudness.
#
#   quiet room    gap is small    0 or 1 LEDs
#   talking       gap is bigger   2 or 3 LEDs
#   shouting      gap is big      4 or 5 LEDs
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
SAMPLES = 50             # how many readings make one measurement
QUIET = 60               # a gap this small counts as a quiet room
LOUD = 1200              # a gap this big is the top of the scale



# ===== 3. FUNCTIONS: the thinking =====
def loudness():
    """SAMPLES readings fast. Loudest minus quietest."""
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
    """Turn a loudness gap into how many LEDs: 0 to 5."""
    # >>>>> YOUR CODE STARTS HERE >>>>>
    # One line. Under QUIET -> 0 LEDs. Over LOUD -> 5 LEDs.
    # In between, spread it out. Same shape as leds_for()
    # in Lesson 3 and angle_for() in Lesson 5.
    return 0
    # <<<<< YOUR CODE ENDS HERE <<<<<


def show(level):
    for i in range(5):
        leds[i].value(1 if i < level else 0)



# ===== 4. THE LOOP: again and again, until you stop it =====
try:
    while True:
        gap = loudness()
        level = level_for(gap)
        print("gap:", gap, "  level:", level)
        show(level)
        time.sleep(0.1)

finally:
    show(0)
    print("Stopped.")

# Try it: whisper, talk, then clap. Write down the gap for each one.
# Try it: QUIET and LOUD are guesses. Change them to fit YOUR room.
