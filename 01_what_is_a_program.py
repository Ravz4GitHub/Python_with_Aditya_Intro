# =============================================================================
# CHAPTER 01 — WHAT IS A PROGRAM?
# =============================================================================
# A program is a set of instructions you give to a computer.
# The computer reads them from top to bottom, one line at a time,
# and does EXACTLY what you say — nothing more, nothing less.
#
# Python is a language that lets you write those instructions in something
# close to plain English. That's why it's the go-to language for AI work.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.1  YOUR FIRST INSTRUCTION — print()
# -----------------------------------------------------------------------------
# print() tells Python to display something on the screen.
# Whatever you put inside the brackets gets shown.

print("Hello, world!")
print("This is Python.")
print("Every line runs one at a time, top to bottom.")


# -----------------------------------------------------------------------------
# 1.2  ORDER MATTERS
# -----------------------------------------------------------------------------
# Python runs your instructions in the exact order you write them.
# Change the order → change the result.

print("Step 1: Open the laptop")
print("Step 2: Connect to Wi-Fi")
print("Step 3: Open the browser")

# Try swapping Step 1 and Step 3 — the program still runs, but the
# instructions no longer make sense. Computers don't "figure it out".


# -----------------------------------------------------------------------------
# 1.3  COMMENTS — notes for humans, ignored by the computer
# -----------------------------------------------------------------------------
# Anything after a # on a line is a comment.
# Python completely ignores it. Comments are for YOU (and your teammates).

# This is a comment — Python skips this line entirely
print("This line runs")  # This part is also a comment

# Good comments explain WHY, not just WHAT.
# Bad comment:  x = x + 1   # adds 1 to x   (we can already see that)
# Good comment: x = x + 1   # move to the next page in the document


# -----------------------------------------------------------------------------
# 1.4  PRINT WITH MULTIPLE THINGS
# -----------------------------------------------------------------------------
# You can print multiple values separated by commas.
# Python automatically adds a space between them.

print("Name:", "Aditya")
print("Score:", 95)
print("Passed:", True)


# -----------------------------------------------------------------------------
# 1.5  WHAT HAPPENS WHEN YOU RUN THIS FILE
# -----------------------------------------------------------------------------
# When you run a Python file, Python starts at line 1 and reads down.
# Every print() produces one line of output.
# When it hits the last line, the program ends and stops.

print("---")
print("Program complete.")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - A program = a list of instructions for the computer
# - Python runs them top to bottom, one at a time
# - print() shows output on the screen
# - # marks a comment — Python ignores it, humans read it
# - Order matters — swap lines and you get different behaviour
# =============================================================================
