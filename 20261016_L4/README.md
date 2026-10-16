# Lesson 4 - Beep! Add sound to the distance meter

## Start of the lesson

```
cd ~/JA05
./get_latest.sh
```

## How to work with the code (Thonny)

Every file in this folder is a complete program. Do not type code from the
slides: the slides only show part of a program, with the file name and line
numbers so you can find it.

Never edit the files in JA05 on your computer. Put a copy on your ESP32 and
edit that copy:

1. Plug in the ESP32. Thonny's bottom-right corner should say MicroPython (ESP32).
2. View > Files.
3. Under "This computer", open JA05 > 20261016_L4.
4. Right-click the step file > Upload to /
5. Double-click the file under "MicroPython device". Edit it there.
   Cmd+S saves it on the ESP32.
6. Click Run (F5). Click Stop to stop.

Change only the lines marked `Try it` or `YOUR CODE`.

Where is GPIO25? On the board it is labelled IO25 (left side). See the
pinout on the "Find your pins" slide.

## Run by itself when the ESP32 starts

When the ESP32 starts it runs `boot.py`, then `main.py`. A file with any other
name, like `step3_parking_beep.py`, only runs when you press Run in Thonny.

1. Upload your `step3_parking_beep.py` to the ESP32.
2. Upload `main.py` from this folder. It contains one line:
   `import step3_parking_beep`
3. Unplug the ESP32 and plug it in again (or use a USB power bank).

Thonny cannot connect while it runs? Click Stop (or Ctrl+C in the Shell).
To stop it starting by itself, delete `main.py` from the ESP32
(right-click > Delete under "MicroPython device").

## Two tracks

**Track A - finish Lesson 3.** Wire the sensor (Lesson 3, Step 4), then upload
and run `20261009_L3/step5_solution.py`. Compare it with your own `leds_for()`.
When the LED bar works, join Track B.

**Track B - add a buzzer.**

| Step | File | Add or change | Checkpoint |
|---|---|---|---|
| 0 | (no code) | Active buzzer: + to 3V3, - to GND | Steady beep as soon as the USB is plugged in |
| 1 | step1_buzzer_on.py | Move the + wire from 3V3 to GPIO25 | Beeps after you run the code |
| 2 | step2_buzzer_beep.py | Nothing | Short beeps, twice a second |
| 3 | step3_parking_beep.py | Nothing. You write gap_for() | Beeps get faster as your hand gets closer |
| 4 | step4_stretch_pitch.py | Swap to the passive buzzer (stretch) | The note gets higher as your hand gets closer |

## Which buzzer is which?

| | Active ("buzzer with power") | Passive ("buzzer without power") |
|---|---|---|
| Underneath | sealed black back | green circuit board |
| + to 3V3, - to GND | steady beep | one click only |
| Code | `buzzer.value(1)` | `PWM(Pin(25), freq=1000, duty=512)` |

Buzzer on a small board with 3 pins? S -> GPIO25, V -> 3V3, G -> GND.

## Pins

| Part | ESP32 pin |
|---|---|
| LED 1 - 5 | GPIO16, 17, 18, 19, 23 |
| Sensor VCC / Trig / Echo / GND | 5V / GPIO13 / GPIO14 / GND |
| Buzzer + | GPIO25 |
| Buzzer - | GND |
