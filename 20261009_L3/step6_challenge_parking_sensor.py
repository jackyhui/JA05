# Step 6 (challenge) - Parking sensor.
#
# Wiring: no change from Step 5.
#
# First: copy your leds_for() from Step 5 into this file (see below).
#
# Same LED bar as Step 5, plus: when something is closer than 5 cm,
# all 5 LEDs flash as a warning. Like the beeping sensor on the back of a car.
#
# Ideas to try:
#   - Flash faster the closer you get.
#   - Use the 1st LED as green, middle as yellow, last as red.
#   - Add the buzzer from the kit.

from machine import Pin, time_pulse_us
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)

SOUND_SPEED = 0.0343
DANGER_CM = 5


def get_distance_cm():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return None
    return duration * SOUND_SPEED / 2


def bar(count):
    for i, led in enumerate(leds):
        led.value(1 if i < count else 0)


# ---------- PASTE YOUR leds_for() FROM STEP 5 HERE ----------
def leds_for(distance):
    if distance is None:
        return 0
    return 0                  # replace with your Step 5 code
# ------------------------------------------------------------


time.sleep(1)
flash_on = False
try:
    while True:
        distance = get_distance_cm()
        if distance is not None and distance < DANGER_CM:
            flash_on = not flash_on
            bar(5 if flash_on else 0)
        else:
            bar(leds_for(distance))
        time.sleep(0.1)
finally:
    bar(0)
