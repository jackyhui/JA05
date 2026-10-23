# Step 0 - What is a function? No wiring needed.
#
# You have been using functions since Lesson 1 without calling them that:
#   print(...)        someone else wrote it
#   time.sleep(...)   someone else wrote it
#   leds_for(...)     YOU wrote it
#
# A function is a named piece of code. You give it something, it gives
# something back. Run this file and read the Shell from top to bottom.

print("1. The program starts here")


def greet(name):
    print("   Hello,", name)


print("2. greet is DEFINED. No hello yet.")

greet("Class 2A")
greet("Ms Chan")

print("3. Two hellos: greet was CALLED twice.")


# This one does not print. It GIVES BACK a number.
def leds_for(distance):
    return max(0, min(5, 5 - int(distance // 5)))


print("4. distance -> how many LEDs")
for d in [40, 22, 12, 7, 2]:
    print("  ", d, "cm ->", leds_for(d), "LEDs")

answer = leds_for(12)
print("5. leds_for(12) gave back", answer)

# Try it: add 17 to the list on line 31. Predict the answer first.
# Try it: on line 20, change "Class 2A" to your own name.
# Try it: delete the two greet(...) lines. What does the Shell show now?
