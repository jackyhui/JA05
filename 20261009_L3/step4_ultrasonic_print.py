# Step 4 - Read the ultrasonic sensor (HC-SR04) and print the distance.
#
# Keep the 5 LEDs plugged in. Just ADD the sensor:
#   Sensor VCC  -> 5V
#   Sensor GND  -> GND
#   Sensor Trig -> GPIO13
#   Sensor Echo -> GPIO14
#
# Point the sensor at your hand and move it closer and further.
# Stop the program with Ctrl+C.

from machine import Pin, time_pulse_us
import time

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)

SOUND_SPEED = 0.0343     # sound travels 0.0343 cm in 1 microsecond (343 m/s)


def get_distance_cm():
    # 1. Send a 10 microsecond pulse on Trig. The sensor sends 8 "clicks" of sound.
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # 2. Echo stays HIGH while the sound travels out and back.
    #    Wait at most 30000 us (about 5 m). Gives a negative number if no echo.
    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return None

    # 3. The sound went there AND back, so divide by 2.
    return duration * SOUND_SPEED / 2


time.sleep(1)            # let the sensor settle
while True:
    distance = get_distance_cm()
    if distance is None:
        print("No echo - nothing in front, or check Trig/Echo wires")
    else:
        print("Distance: {:.1f} cm".format(distance))
    time.sleep(0.2)
