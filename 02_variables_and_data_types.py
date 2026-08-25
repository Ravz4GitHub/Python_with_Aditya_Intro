# =============================================================================
# CHAPTER 02 — VARIABLES & DATA TYPES
# =============================================================================
# A variable is a named container that holds a value.
# Think of it like a labeled box — you put something inside,
# give the box a name, and refer to it by that name later.
#
# Data types tell Python WHAT KIND of value is stored.
# Python uses the type to decide what operations make sense.
# =============================================================================


# -----------------------------------------------------------------------------
# 2.1  CREATING VARIABLES
# -----------------------------------------------------------------------------
# Syntax: variable_name = value
# The = sign means "assign this value to this name".
# It does NOT mean "equals" in the math sense.

name = "Aditya"
age = 21
company = "Anthropic"

print(name)
print(age)
print(company)


# -----------------------------------------------------------------------------
# 2.2  THE FOUR BASIC DATA TYPES
# -----------------------------------------------------------------------------

# --- str (string) — any text, always inside quotes ---
first_name = "Rohan"
job_title = "Director of Operations"
message = "Welcome to the AI training session!"

# --- int (integer) — whole numbers, no decimal point ---
employees = 250
year = 2025
floor = 7

# --- float — numbers with a decimal point ---
growth_rate = 2.7
tax_rate = 0.18
temperature = 36.6

# --- bool (boolean) — ONLY True or False (capital T and F) ---
is_active = True
has_access = False
session_open = True

# You can check what type a variable is:
print(type(first_name))  # <class 'str'>
print(type(employees))  # <class 'int'>
print(type(growth_rate))  # <class 'float'>
print(type(is_active))  # <class 'bool'>


# -----------------------------------------------------------------------------
# 2.3  USING VARIABLES TOGETHER
# -----------------------------------------------------------------------------
# Once a variable holds a value, you can use it anywhere.

name = "Ananya"
score = 88
passed = True

print("Name:", name)
print("Score:", score)
print("Passed:", passed)

# You can do math with int and float variables:
base_salary = 50000
bonus = 8000
total = base_salary + bonus
print("Total compensation:", total)  # → 58000


# -----------------------------------------------------------------------------
# 2.4  VARIABLES CAN BE UPDATED
# -----------------------------------------------------------------------------
# The value in a variable can change — that's why they're called variables.

counter = 0
print("Start:", counter)

counter = counter + 1  # take the current value, add 1, store it back
print("After +1:", counter)

counter = counter + 1
print("After +1 again:", counter)

# Shorthand for the same thing:
counter += 1  # means: counter = counter + 1
print("After += 1:", counter)


# -----------------------------------------------------------------------------
# 2.5  THE TYPE TRAP — strings vs numbers
# -----------------------------------------------------------------------------
# "5" and 5 look the same to a human but mean different things to Python.

number_five = 5  # int — can do math
string_five = "5"  # str — text that happens to look like a number

print(number_five + 3)  # → 8   (math)
print(string_five + "3")  # → "53" (joins text together — called concatenation)

# This is one of the most common sources of confusion for beginners.
# Always be aware of what type your variable holds.

# You can convert between types:
converted = int(string_five)  # turns "5" into 5
print(converted + 3)  # → 8  (now it's math)

age_number = 34
age_text = str(age_number)  # turns 34 into "34"
print("I am " + age_text + " years old")  # joins strings together


# -----------------------------------------------------------------------------
# 2.6  NAMING RULES FOR VARIABLES
# -----------------------------------------------------------------------------
# Good variable names make code readable. Follow these conventions:

# USE: lowercase with underscores (called snake_case)
employee_name = "Dev"
total_sessions = 12
is_completed = False

# AVOID: names that are confusing or meaningless
x = "Dev"  # what is x? nobody knows
a1 = 12  # cryptic
data = False  # too vague — data of what?

# CANNOT USE: Python reserved keywords as variable names
# if, else, for, while, class, def, return, True, False, None, import, ...
# These have special meaning in Python. Using them causes an error.

# CANNOT START with a number:
# 1name = "test"   ← this would be an error


# -----------------------------------------------------------------------------
# 2.7  NONE — the "nothing" value
# -----------------------------------------------------------------------------
# None is a special value that means "no value yet" or "empty".
# It's its own type, called NoneType.

result = None
print(result)  # → None
print(type(result))  # → <class 'NoneType'>

# Useful when you want a variable to exist but don't have a value for it yet:
pending_response = None  # will be filled in later


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - Variable = a named box that holds a value
# - = assigns a value; it does NOT mean "equals"
# - The 4 types: str (text), int (whole number), float (decimal), bool (T/F)
# - "5" ≠ 5 — string vs integer behaves differently
# - Use int(), str(), float() to convert between types
# - None means "no value"
# - Use snake_case for variable names
# =============================================================================
