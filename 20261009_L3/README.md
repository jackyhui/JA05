# Lesson 3 - How far away? Ultrasonic sensor + LED bar

Build it one small step at a time. Do not move on until the checkpoint works.
If something breaks, go back ONE step. That step worked before, so it will work again.

| Step | File | Add or change | Checkpoint |
|---|---|---|---|
| 0 | (no code) | 3V3 -- 220 ohm -- LED -- GND | LED is ON as soon as the USB is plugged in |
| 1 | step1_led_on.py | Move the 3V3 wire to GPIO16 | LED is ON after you run the code |
| 2 | step2_led_blink.py | Nothing | LED blinks every 0.5 s |
| 3a | step3a_check_leds.py | 4 more LEDs on GPIO17, 18, 19, 23 | LED 1 to 5 light one by one |
| 3b | step3b_led_patterns.py | Nothing | Chase, bar, and blink patterns |
| 4 | step4_ultrasonic_print.py | Sensor: VCC-5V, GND-GND, Trig-GPIO13, Echo-GPIO14 | Shell prints a distance that changes with your hand |
| 5 | step5_distance_leds.py | Nothing. You write leds_for() | Closer hand = more LEDs on, matching the table |
| 6 | step6_challenge_parking_sensor.py | Paste your leds_for() from Step 5 (challenge) | LEDs flash when closer than 5 cm |

## Pins

| Part | ESP32 pin |
|---|---|
| LED 1 | GPIO16 |
| LED 2 | GPIO17 |
| LED 3 | GPIO18 |
| LED 4 | GPIO19 |
| LED 5 | GPIO23 |
| Sensor VCC | 5V |
| Sensor Trig | GPIO13 |
| Sensor Echo | GPIO14 |
| Sensor GND, all LED short legs | GND |

Every LED: GPIO -- 220 ohm resistor -- LED long leg (+), LED short leg (-) -- GND.
Never connect an LED without a resistor.

## Run a step

```
mpremote connect /dev/cu.usbserial-0001 run step1_led_on.py
```

Stop a running program with Ctrl+C.
