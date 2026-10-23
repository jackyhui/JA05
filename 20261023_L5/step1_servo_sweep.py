# Step 1 - Make the servo move. Three positions.
#
# A servo is a motor that goes to an ANGLE and stays there.
# You tell it 0, 90 or 180 degrees, not "spin".
#
# WIRING - get this right before you run anything:
#   Servo brown (or black) wire  -> GND
#   Servo red wire               -> 5V      (NOT 3V3)
#   Servo orange (or yellow)     -> GPIO26  (IO26 on the board)
#
# Keep the LEDs, the sensor and the buzzer from Lessons 3 and 4 plugged in.
#
# Put the white plastic arm (the "horn") on the servo loosely for now.
#
# Stop the program with Ctrl+C.

from machine import Pin, PWM
import time

servo = PWM(Pin(26))
servo.freq(50)            # a servo listens 50 times a second

#   angle    duty_u16
#      0       1638
#     90       4915
#    180       8100

try:
    servo.duty_u16(1638)      # 0 degrees
    print("0 degrees")
    time.sleep(1)

    servo.duty_u16(4915)      # 90 degrees
    print("90 degrees")
    time.sleep(1)

    servo.duty_u16(8100)      # 180 degrees
    print("180 degrees")
    time.sleep(1)

    servo.duty_u16(1638)      # back to 0
    print("back to 0 degrees")
    time.sleep(1)

    # Try it: add one more line here that sends it to 90 degrees.

finally:
    servo.deinit()            # stop sending pulses
