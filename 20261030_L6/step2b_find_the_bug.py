# Step 2b - Find the bug. Five minutes, in pairs. No wiring needed.
#
# WHAT YOU DO: find ONE wrong line and move it. Do not rewrite.
#
# This program is supposed to count how many loud moments happen in a list
# of readings. The right answer is 3. The program says something else.
#
# Do NOT rewrite it. Use the ladder:
#   1. Run it. What number does it print?
#   2. Put a print() inside the loop so you can see count change.
#   3. Which line throws away what the program already knew?
#   4. Change ONE line. Run again.

readings = [1, 2, 8, 9, 1, 7, 1, 1, 6, 6, 2]
LOUD = 5

was_loud = False

for value in readings:
    count = 0
    is_loud = value > LOUD
    if is_loud and not was_loud:
        count = count + 1
    was_loud = is_loud

print("Loud moments:", count)
print("The right answer is 3.")
