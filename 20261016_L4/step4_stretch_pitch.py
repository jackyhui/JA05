# Step 4 (stretch) - Change the PITCH with distance. Closer = higher note.
#
# Swap to the PASSIVE buzzer ("buzzer without power", green board underneath).
# It goes in the same place as the active buzzer:
#   GPIO25 -- buzzer + ,  buzzer - -- GND
#
# A passive buzzer only makes a sound when the pin switches on and off very
# fast. PWM does that for us. freq = how many times per second (Hz).
#   low number  (200 Hz)  = low note
#   high number (2000 Hz) = high note
#
# Stop the program with Ctrl+C.

from machine import Pin, PWM, time_pulse_us
import time

PINS = [16, 17, 18, 19, 23]
leds = [Pin(p, Pin.OUT) for p in PINS]

trig = Pin(13, Pin.OUT, value=0)
echo = Pin(14, Pin.IN)
buzzer = PWM(Pin(25), freq=1000, duty=0)   # duty 0 = silent, 512 = sound

SOUND_SPEED = 0.0343


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
    if distance is None:
        return 0
    return max(0, min(5, 5 - int(distance // 5)))


def pitch_for(distance):
    # 25 cm -> 300 Hz (low), 0 cm -> 2300 Hz (high)
    return int(2300 - distance * 80)


time.sleep(1)
try:
    while True:
        distance = get_distance_cm()
        bar(leds_for(distance))
        if distance is None or distance >= 25:
            buzzer.duty(0)                       # quiet
        else:
            buzzer.freq(pitch_for(distance))
            buzzer.duty(512)                     # sound on
            print("Distance: {:5.1f} cm   Pitch: {} Hz".format(distance, pitch_for(distance)))
        time.sleep(0.1)

        # Try it: make the note go DOWN as you get closer.
finally:
    buzzer.deinit()
    bar(0)
