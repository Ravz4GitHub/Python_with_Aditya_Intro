# =============================================================================
# CHAPTER 05 — LOOPS
# =============================================================================
# A loop lets you repeat a block of code multiple times without
# copy-pasting it. Instead of writing 100 print statements,
# you write one and tell Python to repeat it 100 times.
#
# Two types of loops in Python:
#   - for loop   → repeat for each item in a collection
#   - while loop → repeat as long as a condition is True
# =============================================================================


# =============================================================================
# PART A — FOR LOOPS
# =============================================================================
# A for loop goes through a collection (list, string, range, etc.)
# and runs your code block once for each item.
#
# Syntax:
#   for variable_name in collection:
#       code to run for each item
#
# The variable_name is yours to choose. It holds the current item
# on each pass through the loop.
# =============================================================================

# -----------------------------------------------------------------------------
# 5.1  LOOPING OVER A LIST
# -----------------------------------------------------------------------------
employees = ["Ananya", "Dev", "Priya", "Rohan"]

for person in employees:
    print("Welcome,", person)

# Output:
# Welcome, Ananya
# Welcome, Dev
# Welcome, Priya
# Welcome, Rohan

print("---")


# -----------------------------------------------------------------------------
# 5.2  DOING THINGS WITH EACH ITEM
# -----------------------------------------------------------------------------
scores = [78, 92, 55, 88, 100, 63]

total = 0

for score in scores:
    total = total + score    # add each score to our running total

average = total / len(scores)
print("Average score:", average)


# -----------------------------------------------------------------------------
# 5.3  range() — looping a specific number of times
# -----------------------------------------------------------------------------
# range(n) generates the numbers 0, 1, 2, ..., n-1
# range(start, stop) generates from start up to (but not including) stop
# range(start, stop, step) allows custom step size

for i in range(5):
    print("Iteration:", i)    # prints 0, 1, 2, 3, 4

print("---")

for i in range(1, 6):
    print("Step:", i)         # prints 1, 2, 3, 4, 5

print("---")

for i in range(0, 20, 5):
    print("Count:", i)        # prints 0, 5, 10, 15


# -----------------------------------------------------------------------------
# 5.4  LOOPING OVER A STRING
# -----------------------------------------------------------------------------
# A string is a sequence of characters — you can loop over it too.

word = "Claude"

for letter in word:
    print(letter)             # prints C, l, a, u, d, e (one per line)


# -----------------------------------------------------------------------------
# 5.5  LOOPING OVER A DICTIONARY
# -----------------------------------------------------------------------------
config = {
    "model": "claude-3-5-sonnet",
    "temperature": 0.7,
    "max_tokens": 1024
}

# Loop over keys:
for key in config:
    print(key)

print("---")

# Loop over key-value pairs together:
for key, value in config.items():
    print(f"{key}: {value}")


# -----------------------------------------------------------------------------
# 5.6  enumerate() — when you also need the index
# -----------------------------------------------------------------------------
tasks = ["Define scope", "Build prototype", "Run tests", "Deploy"]

for index, task in enumerate(tasks):
    print(f"Task {index + 1}: {task}")

# Output:
# Task 1: Define scope
# Task 2: Build prototype
# Task 3: Run tests
# Task 4: Deploy


# =============================================================================
# PART B — WHILE LOOPS
# =============================================================================
# A while loop keeps running as long as a condition is True.
# Use it when you DON'T know in advance how many times to repeat.
#
# Syntax:
#   while condition:
#       code to run
#       (something here must eventually make the condition False)
#
# WARNING: if the condition never becomes False, you get an infinite loop.
# =============================================================================

# -----------------------------------------------------------------------------
# 5.7  BASIC WHILE LOOP
# -----------------------------------------------------------------------------
count = 1

while count <= 5:
    print("Count:", count)
    count += 1                # CRITICAL: without this, loop runs forever

print("Done counting.")


# -----------------------------------------------------------------------------
# 5.8  WHILE LOOP WITH A FLAG
# -----------------------------------------------------------------------------
# A "flag" is a boolean variable that controls the loop.

authenticated = False
attempts      = 0
max_attempts  = 3

while not authenticated and attempts < max_attempts:
    attempts += 1
    password = "secret123"    # in real code, you'd ask the user to type this

    if password == "secret123":
        authenticated = True
        print(f"Logged in after {attempts} attempt(s).")
    else:
        print(f"Wrong password. Attempts left: {max_attempts - attempts}")

if not authenticated:
    print("Account locked.")


# =============================================================================
# PART C — LOOP CONTROL: break, continue, pass
# =============================================================================

# -----------------------------------------------------------------------------
# 5.9  break — exit the loop immediately
# -----------------------------------------------------------------------------
# When Python hits break, it stops the loop right there and moves on.

numbers = [3, 7, 2, 9, 1, 5, 8]

for num in numbers:
    if num == 9:
        print("Found 9! Stopping search.")
        break
    print("Checking:", num)


# -----------------------------------------------------------------------------
# 5.10 continue — skip THIS iteration, continue to the next
# -----------------------------------------------------------------------------
# When Python hits continue, it skips the rest of this pass
# and goes directly to the next item in the loop.

for i in range(10):
    if i % 2 == 0:    # if even, skip it
        continue
    print(i)           # only odd numbers print


# -----------------------------------------------------------------------------
# 5.11 pass — do nothing (placeholder)
# -----------------------------------------------------------------------------
# pass is used when you need a block syntactically but don't want
# to do anything yet. Common during development.

for item in [1, 2, 3]:
    pass    # "I'll fill this in later"


# =============================================================================
# PART D — COMMON LOOP PATTERNS
# =============================================================================

# -----------------------------------------------------------------------------
# 5.12 BUILDING A NEW LIST with a loop
# -----------------------------------------------------------------------------
prices_ex_tax = [100, 250, 80, 430, 175]
prices_with_tax = []

for price in prices_ex_tax:
    with_tax = price * 1.18
    prices_with_tax.append(with_tax)

print("Prices with tax:", prices_with_tax)


# -----------------------------------------------------------------------------
# 5.13 FILTERING — collecting only items that match a condition
# -----------------------------------------------------------------------------
all_employees = [
    {"name": "Ananya", "department": "Engineering", "level": 5},
    {"name": "Dev",    "department": "Design",      "level": 3},
    {"name": "Priya",  "department": "Engineering", "level": 4},
    {"name": "Rohan",  "department": "HR",          "level": 3},
]

senior_engineers = []

for emp in all_employees:
    if emp["department"] == "Engineering" and emp["level"] >= 4:
        senior_engineers.append(emp["name"])

print("Senior engineers:", senior_engineers)


# -----------------------------------------------------------------------------
# 5.14 NESTED LOOPS — a loop inside a loop
# -----------------------------------------------------------------------------
# The inner loop runs completely for each single iteration of the outer loop.

departments = ["Engineering", "Design"]
levels      = [3, 4, 5]

for dept in departments:
    for level in levels:
        print(f"  {dept} — Level {level}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - for loops go through items in a collection, one at a time
# - while loops run as long as a condition is True
# - range(n) generates numbers — useful for counting loops
# - Always update something in a while loop or it runs forever
# - break stops the loop immediately
# - continue skips to the next iteration
# - Loops are how Claude processes batches: files, messages, results
# =============================================================================
