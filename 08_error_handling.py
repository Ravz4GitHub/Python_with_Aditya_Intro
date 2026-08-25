# =============================================================================
# CHAPTER 08 — ERROR HANDLING
# =============================================================================
# Errors (called Exceptions in Python) happen when the program encounters
# something it can't do. Without handling them, the program CRASHES.
#
# Error handling lets you:
#   - Catch an error before it crashes the program
#   - Show a helpful message instead
#   - Try an alternative approach
#   - Keep the program running
#
# This is essential when working with APIs, files, user input, and networks
# — all the things Claude Code does constantly.
# =============================================================================


# =============================================================================
# PART A — UNDERSTANDING ERRORS
# =============================================================================

# -----------------------------------------------------------------------------
# 8.1  COMMON ERROR TYPES
# -----------------------------------------------------------------------------
# Python has many built-in error types. Each tells you what went wrong.
# Reading the error message is the most important debugging skill.

# NameError — you used a variable that doesn't exist
# print(undefined_variable)     ← NameError: name 'undefined_variable' is not defined

# TypeError — wrong data type for an operation
# result = "hello" + 5          ← TypeError: can only concatenate str (not "int") to str

# ValueError — right type, but the value doesn't make sense
# number = int("hello")         ← ValueError: invalid literal for int() with base 10

# IndexError — you asked for a list position that doesn't exist
# items = [1, 2, 3]
# print(items[10])              ← IndexError: list index out of range

# KeyError — you asked for a dict key that doesn't exist
# data = {"name": "Priya"}
# print(data["age"])            ← KeyError: 'age'

# ZeroDivisionError — dividing by zero
# result = 10 / 0               ← ZeroDivisionError: division by zero

# FileNotFoundError — file path doesn't exist
# open("doesnt_exist.txt")      ← FileNotFoundError: No such file or directory

# AttributeError — object doesn't have that attribute or method
# x = 5
# x.append(1)                   ← AttributeError: 'int' object has no attribute 'append'


# -----------------------------------------------------------------------------
# 8.2  READING AN ERROR MESSAGE
# -----------------------------------------------------------------------------
# Python error messages have a standard structure. Learn to read them.
#
# Traceback (most recent call last):
#   File "script.py", line 12, in <module>
#     result = 10 / 0
# ZeroDivisionError: division by zero
#
# Reading order:
#   1. Start at the BOTTOM — that's the actual error type and message.
#   2. Read the file name and line number to find WHERE it happened.
#   3. Read upward through the traceback to see HOW you got there.


# =============================================================================
# PART B — try / except
# =============================================================================
# Syntax:
#   try:
#       code that might cause an error
#   except ErrorType:
#       code to run if that error occurs
# =============================================================================

# -----------------------------------------------------------------------------
# 8.3  BASIC try / except
# -----------------------------------------------------------------------------
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print("Program continues after the error was caught.")


# -----------------------------------------------------------------------------
# 8.4  CATCHING MULTIPLE ERRORS
# -----------------------------------------------------------------------------
def safe_convert(value):
    """Safely convert a value to an integer."""
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' cannot be converted to an integer.")
        return None
    except TypeError:
        print(f"Input must be a string or number, got {type(value)}")
        return None

print(safe_convert("42"))       # → 42
print(safe_convert("hello"))    # → error message + None
print(safe_convert(None))       # → error message + None
print(safe_convert(3.7))        # → 3 (float truncated to int)


# -----------------------------------------------------------------------------
# 8.5  except Exception — catch anything
# -----------------------------------------------------------------------------
# Sometimes you don't know what error might happen.
# You can catch any exception with the base Exception class.
# Use sparingly — being specific is better.

def risky_operation(data):
    try:
        result = data["score"] / data["attempts"]
        return round(result, 2)
    except Exception as e:         # 'as e' captures the actual error object
        print(f"Something went wrong: {e}")
        return None

print(risky_operation({"score": 90, "attempts": 3}))   # → 30.0
print(risky_operation({"score": 90, "attempts": 0}))   # ZeroDivision
print(risky_operation({"score": 90}))                  # KeyError — 'attempts'
print(risky_operation("wrong input"))                  # TypeError


# -----------------------------------------------------------------------------
# 8.6  else and finally
# -----------------------------------------------------------------------------
# else   → runs ONLY if no exception was raised (the try block succeeded)
# finally → ALWAYS runs, whether or not there was an error — for cleanup

def load_config(filepath):
    """Load a config file safely."""
    file = None
    try:
        file = open(filepath, "r")
        content = file.read()
        print("File loaded successfully.")
        return content
    except FileNotFoundError:
        print(f"Config file not found: {filepath}")
        return None
    except PermissionError:
        print(f"No permission to read: {filepath}")
        return None
    else:
        # Only runs if no exception — rarely used but good to know
        print("No errors occurred.")
    finally:
        # ALWAYS runs — close the file even if there was an error
        if file:
            file.close()
            print("File closed.")

load_config("config.json")          # likely FileNotFoundError
load_config("/etc/hosts")           # real file — may or may not work


# =============================================================================
# PART C — RAISING ERRORS
# =============================================================================

# -----------------------------------------------------------------------------
# 8.7  raise — deliberately trigger an error
# -----------------------------------------------------------------------------
# You can raise exceptions yourself when input doesn't meet your rules.
# This makes your functions communicate failures clearly.

def set_level(level):
    """Set employee level — must be between 1 and 10."""
    if not isinstance(level, int):
        raise TypeError(f"Level must be an integer, got {type(level).__name__}")
    if level < 1 or level > 10:
        raise ValueError(f"Level must be between 1 and 10, got {level}")
    print(f"Level set to: {level}")

try:
    set_level(5)     # fine
    set_level(15)    # raises ValueError
except ValueError as e:
    print(f"Validation error: {e}")

try:
    set_level("five")    # raises TypeError
except TypeError as e:
    print(f"Type error: {e}")


# -----------------------------------------------------------------------------
# 8.8  CUSTOM EXCEPTION CLASSES
# -----------------------------------------------------------------------------
# You can create your own exception types by inheriting from Exception.
# This lets you create domain-specific errors that are easier to catch.

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(
            f"Cannot withdraw {amount}. Balance is only {balance}."
        )


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


account = BankAccount("Priya", 500)

try:
    account.withdraw(200)
    print("Withdrew 200. Balance:", account.balance)
    account.withdraw(400)   # will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"  Requested: {e.amount}, Available: {e.balance}")


# =============================================================================
# PART D — ERROR HANDLING PATTERNS IN THE REAL WORLD
# =============================================================================

# -----------------------------------------------------------------------------
# 8.9  RETRY PATTERN — try again on failure
# -----------------------------------------------------------------------------
import time

def fetch_data_with_retry(url, max_retries=3):
    """Simulate fetching data with automatic retry on failure."""
    for attempt in range(1, max_retries + 1):
        try:
            # In real code: response = requests.get(url)
            # Simulating a failure for demonstration:
            if attempt < 3:
                raise ConnectionError("Network timeout")
            print(f"Success on attempt {attempt}!")
            return {"data": "result"}
        except ConnectionError as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                print(f"Retrying in 1 second...")
                time.sleep(1)
    print("All retries exhausted.")
    return None

result = fetch_data_with_retry("https://api.example.com/data")
print("Final result:", result)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - Exceptions are errors — without handling, they crash the program
# - try/except lets you catch errors and respond gracefully
# - Read error messages bottom-up: type first, then location, then call chain
# - Catch specific exception types when you can (not just bare except)
# - 'except Exception as e' captures the error object for inspection
# - finally always runs — use it for cleanup (closing files, connections)
# - raise lets you trigger your own errors for bad input
# - Custom exception classes make error handling more descriptive
# - Claude Code uses extensive error handling — when it fails, it reads
#   the error, adjusts its approach, and retries. Same pattern as above.
# =============================================================================
