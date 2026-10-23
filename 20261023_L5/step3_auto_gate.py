# Step 3 - The door that opens by itself.
#
# YOUR JOB: finish the function angle_for() below. Everything else is done.
#
# Wiring: Lesson 3 and 4 circuit + the servo from Step 1.
#   LEDs:   GPIO16, 17, 18, 19, 23 -- [220 ohm] -- LED -- GND
#   Sensor: VCC -> 5V, GND -> GND, Trig -> GPIO13, Echo -> GPIO14
#   Buzzer: GPIO25 -- buzzer + ,  buzzer - -- GND
#   Servo:  brown -> GND,  red -> 5V,  orange -> GPIO26
#
#   someone is...        the door...
#   further than 15 cm   stays shut
#   nearer than 15 cm    opens, and stays open for 2 more seconds
#
# Stop the program with Ctrl+C.

from machine import Pin, PWM, time_pulse_us
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)
buzzer = Pin(25, Pin.OUT)

servo = PWM(Pin(26))
servo.freq(50)

SOUND_SPEED = 0.0343     # cm per microsecond

OPEN_ANGLE = 90          # door open
CLOSED_ANGLE = 0         # door shut
NEAR_CM = 15             # someone is standing here
HOLD_LOOPS = 20          # stay open 20 loops = about 2 seconds


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


def set_angle(deg):
    # From Step 2.
    if deg < 0:
        deg = 0
    if deg > 180:
        deg = 180
    servo.duty_u16(int(1638 + deg * 36.4))


def angle_for(distance):
    # Which angle does the door want right now?
    # distance is a number in cm,
    # or None when the sensor saw nothing.

    # ----- YOUR CODE STARTS HERE -----
    # Think: None means nobody is there.
    #        Nearer than NEAR_CM: somebody wants in.
    #        Anything else: stay shut.
    # Use OPEN_ANGLE and CLOSED_ANGLE, not 90 and 0.

    return CLOSED_ANGLE               # replace this line
    # ----- YOUR CODE ENDS HERE -----


time.sleep(1)
hold = 0
try:
    while True:
        distance = get_distance_cm()
        bar(leds_for(distance))

        if angle_for(distance) >= OPEN_ANGLE:
            hold = HOLD_LOOPS         # somebody is there: restart the 2 seconds

        if hold > 0:
            set_angle(OPEN_ANGLE)
            hold = hold - 1
        else:
            set_angle(CLOSED_ANGLE)

        # Try it: add buzzer.value(1) when the door opens, so blind users hear it.

        time.sleep(0.1)
finally:
    set_angle(CLOSED_ANGLE)
    time.sleep(0.5)
    servo.deinit()
    buzzer.value(0)
    bar(0)
