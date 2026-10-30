# Step 2 - A program that remembers. No wiring needed.
#
# WHAT YOU DO: run it. Read the Shell. Change nothing until the
# Try it lines at the bottom.
#
# A loop forgets. Every time round, it does the same lines again with the
# same starting values. If you want it to remember something, YOU have to
# keep that something in a variable that lives OUTSIDE the loop.
#
# A variable like that is called state: what the program knows right now,
# because of what happened before.
#
# Run this file and read the two Shell outputs.

import time

print("WRONG: count is made again every time round the loop")
for round_number in range(1, 6):
    count = 0            # made again, old value lost
    count = count + 1
    print("  round", round_number, "count is", count)

print()
print("RIGHT: count is made ONCE, before the loop")
count = 0                # made once, the loop adds to it
for round_number in range(1, 6):
    count = count + 1
    print("  round", round_number, "count is", count)

print()
print("Remembering the LAST one, to notice a CHANGE")

readings = [2, 2, 7, 8, 2, 9, 9, 2]
LOUD = 5

was_loud = False         # what we knew last time round
shouts = 0

for value in readings:
    is_loud = value > LOUD
    if is_loud and not was_loud:
        shouts = shouts + 1
        print("  ", value, "<- a NEW loud moment starts here")
    else:
        print("  ", value)
    was_loud = is_loud    # today's answer becomes tomorrow's memory

print("Loud readings:", 4, "  but separate loud MOMENTS:", shouts)

# Try it: delete the line  was_loud = is_loud  and run it again.
#         How many shouts does it count now? Why?
# Try it: move  shouts = 0  inside the for loop. What happens?
