# Step 4 - Put the meter on the LCD, so the room can see itself.
#
# WHAT YOU DO: run it. Nothing to write. Stretch task.
#
# Wiring: everything from Step 3, plus the Lesson 1 LCD.
#   Sound sensor: V -> 3V3, G -> GND, S -> GPIO36
#   LEDs:         GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#   LCD:          SDA -> GPIO21, SCL -> GPIO22, V -> 5V, G -> GND
#
# Upload lcd128_32.py and lcd128_32_fonts.py as well, or the import fails.
#
# The counting code is the same as Step 3. The only new part is the screen.
# Refreshing the LCD is slow, so we only redraw when something changed.
#
# Stop the program with Ctrl+C.

from machine import ADC, Pin
from lcd128_32 import lcd128_32
import time

# ===== 1. SETUP: the pins and the sensor =====
PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

mic = ADC(Pin(36))
mic.atten(ADC.ATTN_11DB)
mic.width(ADC.WIDTH_12BIT)

lcd = lcd128_32(21, 22, 0, 0x3F)


# ===== 2. NUMBERS YOU CAN CHANGE =====
SAMPLES = 50
QUIET = 60
LOUD = 1200
TOO_LOUD_LEVEL = 4
COOLDOWN = 2.0



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
    if gap <= QUIET:
        return 0
    if gap >= LOUD:
        return 5
    return 1 + int((gap - QUIET) * 4 / (LOUD - QUIET))


def show(level):
    for i in range(5):
        leds[i].value(1 if i < level else 0)


def draw(level, count):
    """Redraw the LCD. 4 rows, 18 characters each."""
    lcd.Clear()
    lcd.Cursor(0, 0)
    lcd.Display("Noise level: " + str(level))
    lcd.Cursor(1, 0)
    lcd.Display("[" + "#" * level + "." * (5 - level) + "]")
    lcd.Cursor(2, 0)
    lcd.Display("Too loud: " + str(count))



# ===== 4. THE MEMORY: made once, before the loop =====
loud_count = 0
was_loud = False
last_count_time = 0
last_drawn = None


# ===== 5. THE LOOP: again and again, until you stop it =====
try:
    draw(0, 0)
    while True:
        gap = loudness()
        level = level_for(gap)
        show(level)

        is_loud = level >= TOO_LOUD_LEVEL
        now = time.time()
        if is_loud and not was_loud and now - last_count_time >= COOLDOWN:
            loud_count = loud_count + 1
            last_count_time = now
        was_loud = is_loud

        # Only touch the screen when the numbers actually changed.
        if (level, loud_count) != last_drawn:
            draw(level, loud_count)
            last_drawn = (level, loud_count)

        time.sleep(0.1)

finally:
    show(0)
    lcd.Clear()
    lcd.Cursor(0, 0)
    lcd.Display("Session ended")
    lcd.Cursor(1, 0)
    lcd.Display("Too loud: " + str(loud_count))
    print("Stopped. Loud moments this session:", loud_count)

# Try it: the LCD row is 18 characters. Add the gap number and see what is cut off.
# Try it: show the count on row 3 instead, and put your class name on row 0.
