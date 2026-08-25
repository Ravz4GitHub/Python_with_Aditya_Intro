# =============================================================================
# CHAPTER 04 — CONDITIONALS
# =============================================================================
# Conditionals let your program make decisions.
# Based on whether something is True or False, different code runs.
# This is how software branches into different paths.
#
# Real-world analogy: a security gate.
# "IF badge is valid → let them in. ELSE → show error."
# The gate checks the condition and picks a path.
# =============================================================================


# -----------------------------------------------------------------------------
# 4.1  THE BASIC if STATEMENT
# -----------------------------------------------------------------------------
# Syntax:
#   if condition:
#       code to run if condition is True
#
# The colon : and the indentation (4 spaces) are NOT optional.
# Python uses indentation to know what's "inside" the if block.

temperature = 38

if temperature > 37:
    print("You have a fever.")
    print("Please rest and drink water.")

print("This line always runs — it's outside the if block.")


# -----------------------------------------------------------------------------
# 4.2  if / else — two paths
# -----------------------------------------------------------------------------
# If the condition is True → run the if block.
# If the condition is False → run the else block.

score = 65

if score >= 70:
    print("Passed!")
else:
    print("Needs improvement.")

# Only one of these two lines will ever print — never both.


# -----------------------------------------------------------------------------
# 4.3  if / elif / else — multiple paths
# -----------------------------------------------------------------------------
# elif = "else if" — check another condition if the first one is False.
# You can chain as many elif blocks as you need.

score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"       # ← this runs (82 is between 80 and 89)
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"       # only runs if ALL conditions above are False

print("Grade:", grade)

# Python checks from top to bottom and STOPS at the first True condition.
# Once a match is found, the rest of elif/else are skipped.


# -----------------------------------------------------------------------------
# 4.4  COMPARISON OPERATORS
# -----------------------------------------------------------------------------
# These compare two values and always return True or False.

x = 10

print(x == 10)    # True   — equal to
print(x != 5)     # True   — not equal to
print(x > 8)      # True   — greater than
print(x < 5)      # False  — less than
print(x >= 10)    # True   — greater than or equal to
print(x <= 9)     # False  — less than or equal to

# IMPORTANT: = vs ==
# =   means ASSIGN (put a value into a variable)
# ==  means COMPARE (are these two things equal?)
#
# This is one of the most common beginner mistakes:
# if x = 10:    ← WRONG — this is an error
# if x == 10:   ← CORRECT


# -----------------------------------------------------------------------------
# 4.5  LOGICAL OPERATORS — combining conditions
# -----------------------------------------------------------------------------
# and  → BOTH conditions must be True
# or   → AT LEAST ONE condition must be True
# not  → flips True to False, and False to True

age = 28
has_id = True

# and
if age >= 18 and has_id:
    print("Entry allowed.")

# or
is_member = False
is_vip = True

if is_member or is_vip:
    print("Access granted.")

# not
is_banned = False

if not is_banned:
    print("User is allowed.")

# Combining them — use parentheses to make intent clear:
balance = 500
credit_limit = 1000
is_premium = True

if (balance < 100 or credit_limit < 200) and not is_premium:
    print("Restrict access.")
else:
    print("Access OK.")


# -----------------------------------------------------------------------------
# 4.6  CHECKING FOR MEMBERSHIP — the in operator
# -----------------------------------------------------------------------------
# You can check if a value exists inside a list or string.

allowed_roles = ["admin", "editor", "moderator"]
user_role = "editor"

if user_role in allowed_roles:
    print(f"{user_role} has permission.")
else:
    print(f"{user_role} does not have permission.")

# Works on strings too:
email = "priya@company.com"

if "@" in email:
    print("Looks like a valid email format.")


# -----------------------------------------------------------------------------
# 4.7  TRUTHY AND FALSY VALUES
# -----------------------------------------------------------------------------
# In Python, many values are treated as True or False in a condition,
# even if they're not actually booleans.
#
# FALSY (treated as False):
#   - False
#   - 0
#   - "" (empty string)
#   - [] (empty list)
#   - {} (empty dict)
#   - None
#
# Everything else is TRUTHY (treated as True).

name = ""
if name:
    print("Name is:", name)
else:
    print("No name provided.")    # ← this runs because "" is falsy

items = [1, 2, 3]
if items:
    print("List has items.")      # ← this runs because the list is truthy

empty_list = []
if not empty_list:
    print("List is empty!")       # ← this runs because [] is falsy


# -----------------------------------------------------------------------------
# 4.8  REAL-WORLD EXAMPLE — access control system
# -----------------------------------------------------------------------------
def check_access(username, role, hours_active):
    """Decide if a user can access the system."""

    if username == "":
        print("Error: No username provided.")
        return

    if role not in ["admin", "staff", "viewer"]:
        print(f"Error: Unknown role '{role}'.")
        return

    if hours_active > 8:
        print(f"Session expired for {username}. Please log in again.")
        return

    if role == "admin":
        print(f"Welcome, {username}. Full access granted.")
    elif role == "staff":
        print(f"Welcome, {username}. Standard access granted.")
    else:
        print(f"Welcome, {username}. Read-only access granted.")


# Test it:
check_access("priya",  "admin",  3)
check_access("rohan",  "staff",  7)
check_access("guest1", "viewer", 9)    # session expired
check_access("",       "admin",  1)    # no username


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - if runs a block only if a condition is True
# - else runs if none of the conditions above were True
# - elif lets you check multiple conditions in sequence
# - Python stops at the FIRST True condition — the rest are skipped
# - Comparison operators: == != > < >= <=
# - = is assignment, == is comparison (don't mix them up)
# - Logical operators: and, or, not
# - in checks if a value exists inside a list or string
# - Empty values (0, "", [], {}, None) are falsy
# =============================================================================
