# Step 2 - Say the angle you want, not the duty number.
#
# Wiring: no change from Step 1.
#   Servo brown -> GND,  red -> 5V,  orange -> GPIO26
#
# In Step 1 you had to remember 1638, 4915, 8100. Nobody can remember that.
# set_angle() does the maths for you, so you can write set_angle(90).
#
# Stop the program with Ctrl+C.

from machine import Pin, PWM
import time

servo = PWM(Pin(26))
servo.freq(50)

MIN_DUTY = 1638           # 0 degrees
STEP_PER_DEGREE = 36.4    # (8190 - 1638) / 180


def set_angle(deg):
    if deg < 0:
        deg = 0           # never ask for less than 0
    if deg > 180:
        deg = 180         # never ask for more than 180
    duty = MIN_DUTY + deg * STEP_PER_DEGREE
    servo.duty_u16(int(duty))


try:
    for angle in [0, 45, 90, 135, 180, 90, 0]:
        print("angle:", angle)
        set_angle(angle)
        time.sleep(0.8)

        # Try it: put your own angles in the list on line 32.
        # Try it: change 0.8 to 0.2. The servo moves faster.

finally:
    servo.deinit()
