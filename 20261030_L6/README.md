# Lesson 6 — The classroom noise meter

30 October 2026.

You already have a device that senses, decides, and acts. Today it learns to
**remember**: how loud the room is right now, and how many times it has been
too loud since the program started.

## Wiring

| Part | Pin |
|---|---|
| Sound sensor **V** | 3V3 |
| Sound sensor **G** | GND |
| Sound sensor **S** (the analog output) | GPIO36 |
| LEDs ×5, each through a 220 ohm resistor | GPIO16, 17, 18, 19, 23 |
| LCD SDA / SCL (Step 4 only) | GPIO21 / GPIO22 |

The module runs on 3.3 V or 5 V, but use **3V3**: GPIO36 must never see more
than 3.3 V.

GPIO36 is input-only, and it keeps working when Wi-Fi is on. Do not move the
sensor to GPIO25, 26 or 27.

### The blue screw sets the signal size, not a threshold

It sets how big the signal reaching **S** is. It does not decide "how loud
counts as loud" — your code does that. Set it once with Step 0b and leave it,
or your numbers stop meaning anything from one run to the next.

On this module the output is clamped, so a quiet room reads near **0** and
sound shows up as spikes upward. That is why the manufacturer's own example
calls anything over 600 "sound".

## How to read these files

Every file starts with a line that says **WHAT YOU DO**. Four of the seven are
run-and-read: running them unchanged *is* the work.

Every file is built in the same five parts, with a banner comment on each:

```
# ===== 1. SETUP: the pins and the sensor =====
# ===== 2. NUMBERS YOU CAN CHANGE =====
# ===== 3. FUNCTIONS: the thinking =====
# ===== 4. THE MEMORY: made once, before the loop =====
# ===== 5. THE LOOP: again and again, until you stop it =====
```

You only ever touch part 3 or part 5, and only between these markers:

```
# >>>>> YOUR CODE STARTS HERE >>>>>
# <<<<< YOUR CODE ENDS HERE <<<<<
```

Scroll until you see the arrows. If a file has none, there is nothing to write
in it.

## Steps

| Step | File | What you do | Checkpoint |
|---|---|---|---|
| 0 | step0_read_sound.py | Run it. Clap | The number jumps when you clap |
| 0b | step0b_test_parts.py | Run it. Answer three questions with your eyes | All 3 tests pass |
| 1 | step1_peak_level.py | Write `level_for()` | LED bar follows your voice |
| 2 | step2_counter_demo.py | Run it. No wiring | You can say why one count stays at 1 |
| 2b | step2b_find_the_bug.py | Find one line. Five minutes, in pairs | It prints 3 |
| 3 | step3_noise_counter.py | Write the two counting lines | One clap adds exactly 1 |
| 4 | step4_lcd_report.py | Upload the two lcd128_32 files too | The room can read its own count |

## State: the idea of the day

A loop forgets. Every round it runs the same lines again. Anything the program
must still know next round has to live in a variable made **before** the loop.

```python
count = 0                 # made ONCE, outside the loop
while True:
    count = count + 1     # the same box, added to
```

Put `count = 0` inside the loop instead and the count never passes 1, because
the old value is thrown away every round.

Two pieces of memory make Step 3 work:

- `loud_count` — how many loud moments so far.
- `was_loud` — was the room loud **last** time round? Without it you count
  readings, not moments, and one shout counts forty times.

## When it does not work

In this order. Do not skip to the bottom.

1. **Does it run at all?** Red text in the Shell ends with a line number. Open
   that line first.
2. **Go back to the last version that worked.** If Step 2 ran and Step 3 does
   not, the bug is inside what you changed. Not somewhere mysterious.
3. **Change one thing, then run.** Two changes at once and you learn nothing
   from the result.
4. **Cut the program in half.** Is the problem the input, the decision, or the
   output?
   - Input and output: run `step0b_test_parts.py`.
   - Decision: call the function with a number you pick. `print(level_for(500))`
     needs no sensor and no noise at all.
5. **Make the invisible visible.** `print()` the value you are guessing about.
   Most bugs today are a variable holding something nobody looked at.

Starting over is not step 6. Copy the last file that worked and re-apply your
change in smaller pieces.

## Honest about the number

This sensor is not calibrated. It measures the gap between the quietest and
loudest sample, which follows loudness but is not decibels. Call it **level 0
to 5**. Do not call it dB — a phone app will disagree with you, and the phone
will be right.

`QUIET = 60` and `LOUD = 1200` in the code are starting guesses, made with a
different module and a different screw setting. Measure your own room with Step 0b and change them.
Two groups with different gain settings will get different numbers for the
same noise, and both are right.
