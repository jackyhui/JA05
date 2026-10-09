# Step 5 - Show the distance on 5 LEDs. Closer = more LEDs on.
#
# YOUR JOB: finish the function leds_for() below. Everything else is done.
#
# Wiring: no change from Step 4.
#   LEDs:   GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#   Sensor: VCC -> 5V, GND -> GND, Trig -> GPIO13, Echo -> GPIO14
#
#   distance      LEDs on
#   under  5 cm   5
#   under 10 cm   4
#   under 15 cm   3
#   under 20 cm   2
#   under 25 cm   1
#   25 cm or more 0
#
# Stop the program with Ctrl+C.

from machine import Pin, time_pulse_us
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)

SOUND_SPEED = 0.0343     # cm per microsecond


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
    # Light the first "count" LEDs
    for i, led in enumerate(leds):
        led.value(1 if i < count else 0)


def leds_for(distance):
    # Turn a distance into a number of LEDs (0 to 5). Use the table at the top.
    if distance is None:      # no echo -> nothing close -> 0 LEDs
        return 0

    # ---------- YOUR CODE STARTS HERE ----------
    # Hint: start with the closest case, then work outwards.
    #     if distance < 5:
    #         return 5
    #     elif distance < 10:
    #         return ...
    #
    # Test: the Shell prints the distance and the number of LEDs.
    # Does it match the table?

    return 0                  # replace this line
    # ---------- YOUR CODE ENDS HERE ----------


time.sleep(1)
try:
    while True:
        distance = get_distance_cm()
        count = leds_for(distance)
        bar(count)
        if distance is None:
            print("No echo   LEDs: 0")
        else:
            print("Distance: {:5.1f} cm   LEDs: {}".format(distance, count))
        time.sleep(0.1)
finally:
    bar(0)
