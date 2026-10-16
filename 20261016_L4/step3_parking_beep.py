# Step 3 - Parking sensor with sound. Closer = faster beeps.
#
# YOUR JOB: finish the function gap_for() below. Everything else is done.
#
# Wiring: Lesson 3 circuit + the buzzer from Step 1.
#   LEDs:   GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#   Sensor: VCC -> 5V, GND -> GND, Trig -> GPIO13, Echo -> GPIO14
#   Buzzer: GPIO25 -- buzzer + ,  buzzer - -- GND
#
#   distance        sound
#   25 cm or more   quiet
#   5 to 25 cm      beep ... beep   (closer = shorter gap)
#   under 5 cm      one long beep
#
# Stop the program with Ctrl+C.

from machine import Pin, time_pulse_us
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)
buzzer = Pin(25, Pin.OUT)

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
    for i, led in enumerate(leds):
        led.value(1 if i < count else 0)


def leds_for(distance):
    # From Lesson 3 (see 20261009_L3/step5_solution.py)
    if distance is None:
        return 0
    return max(0, min(5, 5 - int(distance // 5)))


def gap_for(distance):
    # How long to stay quiet between two beeps, in seconds.
    # distance is always between 5 and 25 cm here.

    # ----- YOUR CODE STARTS HERE -----
    # Hint: a bigger distance should give a bigger gap.
    #     20 cm -> about 0.4 s
    #     10 cm -> about 0.2 s
    #      5 cm -> about 0.1 s
    # What do you multiply the distance by?

    return 0.5                # replace this line
    # ----- YOUR CODE ENDS HERE -----


time.sleep(1)
try:
    while True:
        distance = get_distance_cm()
        bar(leds_for(distance))

        if distance is None or distance >= 25:
            buzzer.value(0)            # nothing close: quiet
            time.sleep(0.1)
        elif distance < 5:
            buzzer.value(1)            # very close: long beep
            time.sleep(0.1)
        else:
            buzzer.value(1)            # short beep
            time.sleep(0.05)
            buzzer.value(0)
            time.sleep(gap_for(distance))
finally:
    buzzer.value(0)
    bar(0)
