# Lesson 5 - The door that opens by itself

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
3. Under "This computer", open JA05 > 20261023_L5.
4. Right-click the step file > Upload to /
5. Double-click the file under "MicroPython device". Edit it there.
   Cmd+S saves it on the ESP32.
6. Click Run (F5). Click Stop to stop.

Change only the lines marked `Try it` or `YOUR CODE`.

## Wire the servo - read this before you plug anything in

| Servo wire | Goes to |
|---|---|
| brown (or black) | GND |
| red | **5V** - never 3V3 |
| orange (or yellow) | GPIO26 (IO26 on the board) |

A servo pulls far more current than an LED. On 3V3 it browns out the ESP32 and
Thonny disconnects in the middle of the lesson.

Hold the servo body in your hand or tape it down. If it is loose it walks off
the table while it moves.

## Two tracks

**Track A - catch up.** Wire the sensor (Lesson 3, Step 4) and run
`20261009_L3/step5_solution.py`. When the LED bar works, join Track B at Step 1.
You do not need the buzzer to start Lesson 5.

**Everybody starts with Step 0.** It needs no wiring, so you can do it while
your partner finishes the wiring.

| Step | File | Add or change | Checkpoint |
|---|---|---|---|
| 0 | step0_functions.py | Nothing. Run it and read the Shell | Message 2 appears before any hello |
| 1 | step1_servo_sweep.py | Wire the servo | The horn jumps to 3 positions |
| 2 | step2_servo_angle.py | Your own angles in the list | It goes to the angle you asked for |
| 3 | step3_auto_gate.py | You write `angle_for()` | Hand near: opens. Hand away: shuts 2 s later |
| 4 | step4_web_gate.py | Type the Wi-Fi name and password | OPEN and CLOSE buttons on your phone |

The Wi-Fi name and password are on the Step 4 slide, and in Lesson 1, slide 14.
Type both into **your copy on the ESP32** (the tab whose name is in square
brackets), not into the file in JA05, then press Cmd+S.

## Before the new project: can you do these?

Tick them honestly. If you cannot tick one, say so in class.

- [ ] I can read a line like `leds_for(12)` and say what it gives back.
- [ ] I can say the difference between writing `def` and calling the function.
- [ ] I can change a number inside a function and predict what happens.
- [ ] I can write the inside of a function when I am told what goes in and what
      comes out.

Questions to try on paper, before you touch a computer:

1. `leds_for(40)` gives back what?
2. `leds_for(2)` gives back what?
3. Which line of your Lesson 3 program decides **when** the LEDs change?
4. `gap_for(20)` gave 0.4 s. What does `gap_for(10)` give?

## What a function is, in three lines

```python
def leds_for(distance):      # def = you are making one. distance is what goes IN
    return 5 - distance // 5 # return = what comes OUT

answer = leds_for(12)        # this line RUNS it. Writing def alone runs nothing.
```

## Run by itself when the ESP32 starts

When the ESP32 starts it runs `boot.py`, then `main.py`. A file with any other
name, like `step3_auto_gate.py`, only runs when you press Run in Thonny.

1. Upload your `step3_auto_gate.py` to the ESP32.
2. Upload `main.py` from this folder. It contains one line:
   `import step3_auto_gate`
3. Unplug the ESP32 and plug it in again (or use a USB power bank).

Thonny cannot connect while it runs? Click Stop (or Ctrl+C in the Shell).
To stop it starting by itself, delete `main.py` from the ESP32
(right-click > Delete under "MicroPython device").

## Pins

| Part | ESP32 pin |
|---|---|
| LED 1 - 5 | GPIO16, 17, 18, 19, 23 |
| Sensor VCC / Trig / Echo / GND | 5V / GPIO13 / GPIO14 / GND |
| Buzzer + | GPIO25 |
| Servo signal (orange) | GPIO26 |
| Servo power (red) | 5V |
| Every minus leg and the servo brown wire | GND |

The sensor and the servo both need 5V. Use the red rail on the breadboard so
one 5V pin feeds both.

## When something goes wrong

| What happens | What to do |
|---|---|
| Thonny disconnects when the servo moves | Red wire must be on 5V, not 3V3. Then unplug and plug in again. |
| Servo buzzes but does not move | It is pushed against something. Free the horn. |
| Servo twitches open and shut | Normal at exactly 15 cm. Move your hand further in or out. |
| Door never opens | `angle_for()` still returns `CLOSED_ANGLE`. Which line did you replace? |
| `TypeError` with `None` | The sensor returns `None` when it sees nothing. Test for `None` first. |
| `Wi-Fi FAILED` | The name or password is wrong. Both need quotes around them. |
| The page does not load | Your phone must be on the class Wi-Fi, not mobile data. |
