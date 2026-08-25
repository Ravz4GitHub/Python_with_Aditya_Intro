# =============================================================================
# CHAPTER 06 — FUNCTIONS
# =============================================================================
# A function is a named, reusable block of code.
# You define it once, then CALL it by name whenever you need it —
# from anywhere, as many times as you want.
#
# Functions solve three problems:
#   1. Repetition   — write the logic once, use it everywhere
#   2. Organisation — break a big program into named, manageable chunks
#   3. Testing      — test one piece of logic independently
#
# Real-world analogy: a coffee machine button.
# Someone engineered "make espresso" once. You just press the button.
# You don't re-engineer it every morning.
# =============================================================================


# -----------------------------------------------------------------------------
# 6.1  DEFINING AND CALLING A FUNCTION
# -----------------------------------------------------------------------------
# def keyword → function name → parentheses → colon → indented body

def greet():
    print("Hello! Welcome to the session.")
    print("Please take a seat.")

# Defining the function does NOT run it.
# You must CALL it to make the code inside run.

greet()    # first call
greet()    # second call — same result, no re-writing


# -----------------------------------------------------------------------------
# 6.2  PARAMETERS — giving input to a function
# -----------------------------------------------------------------------------
# Parameters are variables listed inside the parentheses.
# When you call the function, you pass in values (called arguments).

def greet_person(name):
    print(f"Hello, {name}! Welcome to the session.")

greet_person("Priya")    # name = "Priya"
greet_person("Rohan")    # name = "Rohan"
greet_person("Dev")      # name = "Dev"


# Multiple parameters:
def describe_employee(name, role, years):
    print(f"{name} is a {role} with {years} years of experience.")

describe_employee("Ananya", "Engineer", 6)
describe_employee("Dev",    "Designer", 3)


# -----------------------------------------------------------------------------
# 6.3  RETURN VALUES — getting output from a function
# -----------------------------------------------------------------------------
# return sends a value back to whoever called the function.
# Without return, a function does something but gives nothing back.

def add(a, b):
    result = a + b
    return result

total = add(10, 25)
print("Total:", total)        # → 35
print("Double:", add(7, 7))   # → 14

# You can return any data type:
def get_user_info():
    return {
        "name":  "Priya",
        "role":  "Manager",
        "level": 5
    }

user = get_user_info()
print(user["name"])    # → "Priya"


# -----------------------------------------------------------------------------
# 6.4  DEFAULT PARAMETER VALUES
# -----------------------------------------------------------------------------
# You can give parameters a default value.
# If the caller doesn't provide that argument, the default is used.

def send_notification(message, channel="email", priority="normal"):
    print(f"[{priority.upper()}] Sending via {channel}: {message}")

send_notification("Server is down!")                         # uses defaults
send_notification("Meeting in 5 mins", channel="slack")     # overrides channel
send_notification("Critical error", "sms", "urgent")        # overrides both


# -----------------------------------------------------------------------------
# 6.5  KEYWORD ARGUMENTS — calling by name
# -----------------------------------------------------------------------------
# When calling a function, you can name the arguments explicitly.
# This makes your intent clearer and order doesn't matter.

def create_account(username, email, is_admin=False):
    print(f"Creating account for {username} ({email}). Admin: {is_admin}")

create_account("priya", "priya@co.com")
create_account(email="dev@co.com", username="dev", is_admin=True)


# -----------------------------------------------------------------------------
# 6.6  SCOPE — where variables live
# -----------------------------------------------------------------------------
# Variables created INSIDE a function only exist inside that function.
# This is called LOCAL scope.
# Variables created OUTSIDE functions are in GLOBAL scope.

project_name = "AI Training"    # global — visible everywhere

def show_info():
    team_size = 8               # local — only exists inside this function
    print(f"Project: {project_name}")   # can access the global
    print(f"Team size: {team_size}")    # can access the local

show_info()

# print(team_size)    ← This would cause an error!
# team_size doesn't exist outside the function.


# -----------------------------------------------------------------------------
# 6.7  DOCSTRINGS — documenting your functions
# -----------------------------------------------------------------------------
# A docstring is a string at the top of a function that explains what it does.
# It's the standard way to document Python code.

def calculate_tax(price, rate=0.18):
    """
    Calculate the tax amount for a given price.

    Args:
        price (float): The pre-tax price.
        rate (float):  The tax rate as a decimal. Default is 18% (0.18).

    Returns:
        float: The tax amount (not the total — just the tax).
    """
    return price * rate

# You can access it with help():
help(calculate_tax)   # shows the docstring

print(calculate_tax(1000))         # → 180.0
print(calculate_tax(1000, 0.05))   # → 50.0


# -----------------------------------------------------------------------------
# 6.8  FUNCTIONS CALLING OTHER FUNCTIONS
# -----------------------------------------------------------------------------
# Functions can call other functions. This is how you build programs
# from small, focused pieces. Each function does ONE thing well.

def get_discount(level):
    if level >= 5:
        return 0.20    # 20% discount for senior members
    elif level >= 3:
        return 0.10    # 10% for mid-level
    else:
        return 0.0     # no discount

def calculate_final_price(price, user_level):
    """Calculate the price after discount and tax."""
    discount_rate = get_discount(user_level)         # calls another function
    discounted    = price * (1 - discount_rate)
    tax           = calculate_tax(discounted)        # calls another function
    final         = discounted + tax
    return round(final, 2)

print(calculate_final_price(1000, 5))   # senior user, full discount + tax
print(calculate_final_price(1000, 3))   # mid-level user
print(calculate_final_price(1000, 1))   # no discount


# -----------------------------------------------------------------------------
# 6.9  REAL-WORLD EXAMPLE — text processing (like Claude does it)
# -----------------------------------------------------------------------------
def clean_text(text):
    """Remove extra whitespace and convert to lowercase."""
    return text.strip().lower()

def count_words(text):
    """Return the number of words in a string."""
    words = text.split()    # splits on spaces
    return len(words)

def summarise_input(raw_input):
    """Clean and analyse a text input."""
    cleaned   = clean_text(raw_input)
    word_count = count_words(cleaned)

    return {
        "original":   raw_input,
        "cleaned":    cleaned,
        "word_count": word_count,
        "is_empty":   word_count == 0
    }

user_input = "  Hello Claude, can you help me with my project?  "
result = summarise_input(user_input)

for key, value in result.items():
    print(f"{key}: {value}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - def defines a function; calling it by name runs it
# - Parameters receive input; return sends output back
# - Default values make parameters optional
# - Variables inside a function are LOCAL — they don't exist outside it
# - Docstrings explain what a function does — always write them
# - Functions should each do ONE thing — compose them to build complexity
# - Claude's tools are literally Python functions — same concept
# =============================================================================
