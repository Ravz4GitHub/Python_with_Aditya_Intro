# =============================================================================
# CHAPTER 03 — DATA STRUCTURES
# =============================================================================
# A single variable holds one value. But what if you have 100 names?
# Data structures let you store and organize MANY values in one place.
#
# The three main ones in Python:
#   - List     → ordered, changeable collection
#   - Dictionary → labeled key-value pairs
#   - Tuple    → ordered, LOCKED collection (can't be changed)
# =============================================================================


# =============================================================================
# PART A — LIST
# =============================================================================
# A list holds multiple values in order, inside square brackets [].
# Each value is called an element or item.
# Lists can be changed — you can add, remove, or update items.
#
# Real-world analogy: a to-do list, a shopping list, a list of employees.
# =============================================================================

# -----------------------------------------------------------------------------
# 3.1  CREATING A LIST
# -----------------------------------------------------------------------------
topics = ["variables", "loops", "functions", "classes"]
scores = [88, 95, 72, 100, 63]
mixed  = ["Alice", 30, True, 99.5]   # lists can hold different types

print(topics)
print(scores)


# -----------------------------------------------------------------------------
# 3.2  ACCESSING ITEMS — indexing
# -----------------------------------------------------------------------------
# Each item has a position number called an INDEX.
# IMPORTANT: Python starts counting at 0, not 1.
#
#  topics = ["variables", "loops", "functions", "classes"]
#  index:        0           1          2            3

print(topics[0])    # → "variables"   (first item)
print(topics[1])    # → "loops"       (second item)
print(topics[3])    # → "classes"     (fourth item)

# Negative indexing — count from the END:
print(topics[-1])   # → "classes"     (last item)
print(topics[-2])   # → "functions"   (second to last)


# -----------------------------------------------------------------------------
# 3.3  MODIFYING A LIST
# -----------------------------------------------------------------------------
languages = ["Python", "JavaScript", "Java"]
print("Before:", languages)

languages.append("Go")          # add one item to the end
print("After append:", languages)

languages.insert(1, "Rust")     # insert at a specific position
print("After insert:", languages)

languages.remove("Java")        # remove by value
print("After remove:", languages)

popped = languages.pop()        # removes and returns the last item
print("Popped:", popped)
print("After pop:", languages)

languages[0] = "Python 3"       # update an existing item by index
print("After update:", languages)


# -----------------------------------------------------------------------------
# 3.4  USEFUL LIST OPERATIONS
# -----------------------------------------------------------------------------
numbers = [4, 1, 9, 2, 7, 3]

print("Length:", len(numbers))      # how many items
print("Sum:", sum(numbers))         # total (works on numbers)
print("Max:", max(numbers))         # largest value
print("Min:", min(numbers))         # smallest value

numbers.sort()                      # sort in place (changes the list)
print("Sorted:", numbers)

print("Is 9 in the list?", 9 in numbers)    # → True
print("Is 5 in the list?", 5 in numbers)    # → False


# -----------------------------------------------------------------------------
# 3.5  SLICING — grabbing a portion of a list
# -----------------------------------------------------------------------------
letters = ["a", "b", "c", "d", "e", "f"]

print(letters[1:4])    # → ['b', 'c', 'd']   (from index 1 up to but not including 4)
print(letters[:3])     # → ['a', 'b', 'c']   (from the start up to index 3)
print(letters[3:])     # → ['d', 'e', 'f']   (from index 3 to the end)


# =============================================================================
# PART B — DICTIONARY
# =============================================================================
# A dictionary stores data as KEY → VALUE pairs, inside curly braces {}.
# Instead of a position number, you look things up by a meaningful KEY.
#
# Real-world analogy: a contact card — you look up 'phone' not 'item 3'.
# =============================================================================

# -----------------------------------------------------------------------------
# 3.6  CREATING A DICTIONARY
# -----------------------------------------------------------------------------
person = {
    "name":       "Rohan Sharma",
    "role":       "VP of Engineering",
    "department": "Technology",
    "years":      8,
    "active":     True
}

print(person)


# -----------------------------------------------------------------------------
# 3.7  ACCESSING VALUES
# -----------------------------------------------------------------------------
# Use the key inside square brackets to get its value.

print(person["name"])         # → "Rohan Sharma"
print(person["role"])         # → "VP of Engineering"
print(person["years"])        # → 8

# Safer way — .get() returns None if the key doesn't exist (no error):
print(person.get("salary"))   # → None  (key doesn't exist, no crash)
print(person.get("name"))     # → "Rohan Sharma"


# -----------------------------------------------------------------------------
# 3.8  MODIFYING A DICTIONARY
# -----------------------------------------------------------------------------
employee = {"name": "Ananya", "role": "Designer", "level": 3}

employee["level"] = 4                   # update existing key
employee["team"]  = "Product Design"    # add a new key
del employee["role"]                    # delete a key

print(employee)


# -----------------------------------------------------------------------------
# 3.9  USEFUL DICTIONARY OPERATIONS
# -----------------------------------------------------------------------------
config = {
    "model": "claude-3-5-sonnet",
    "temperature": 0.7,
    "max_tokens": 1024,
    "stream": True
}

print("Keys:  ", list(config.keys()))     # all keys
print("Values:", list(config.values()))   # all values
print("Items: ", list(config.items()))    # key-value pairs as tuples

print("Has 'model' key?", "model" in config)      # → True
print("Has 'api_key' key?", "api_key" in config)  # → False
print("Number of settings:", len(config))          # → 4


# -----------------------------------------------------------------------------
# 3.10 NESTED DICTIONARIES — dictionaries inside dictionaries
# -----------------------------------------------------------------------------
# Very common in real data (JSON from an API looks exactly like this).

user = {
    "id": 1001,
    "profile": {
        "name": "Priya",
        "email": "priya@company.com"
    },
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

print(user["profile"]["name"])             # → "Priya"
print(user["settings"]["notifications"])   # → True


# =============================================================================
# PART C — TUPLE
# =============================================================================
# A tuple is like a list but it CANNOT be changed after creation.
# Written with round brackets ().
# Use it when the data must stay fixed — coordinates, RGB colours, etc.
# =============================================================================

# -----------------------------------------------------------------------------
# 3.11 CREATING AND USING TUPLES
# -----------------------------------------------------------------------------
coordinates  = (12.9716, 77.5946)   # Bengaluru lat/long — shouldn't change
rgb_orange   = (255, 165, 0)        # colour value
http_methods = ("GET", "POST", "PUT", "DELETE")

print(coordinates)
print(coordinates[0])     # → 12.9716 (indexing works the same as lists)
print(coordinates[1])     # → 77.5946

# This would cause an error — tuples are immutable:
# coordinates[0] = 0.0    ← TypeError: 'tuple' object does not support item assignment


# =============================================================================
# PART D — CHOOSING THE RIGHT STRUCTURE
# =============================================================================
#
#  Use a LIST when:
#    - You have an ordered collection of similar items
#    - You'll need to add, remove, or change items
#    - Example: a list of tasks, search results, file names
#
#  Use a DICTIONARY when:
#    - Each piece of data has a meaningful label
#    - You want to look things up by name, not position
#    - Example: a user profile, API config, a JSON response
#
#  Use a TUPLE when:
#    - The data should never change
#    - You want to group related values that belong together
#    - Example: coordinates, a date (year, month, day), RGB values
#
# =============================================================================

# Example — a list of dictionaries (extremely common pattern):
team = [
    {"name": "Ananya", "role": "Engineer",  "level": 4},
    {"name": "Dev",    "role": "Designer",  "level": 3},
    {"name": "Priya",  "role": "Manager",   "level": 5},
]

# Access the second person's role:
print(team[1]["role"])   # → "Designer"

# This pattern — a list of dicts — is exactly what you get back
# from a database query or an API call. It's everywhere in real code.


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - List   [...]  → ordered, changeable. Access by index (starts at 0).
# - Dict   {...}  → key:value pairs. Access by meaningful key name.
# - Tuple  (...)  → ordered, FIXED. Can't be changed after creation.
# - len() gives the count of items in any structure.
# - "item in collection" checks if something exists (returns True/False).
# - Lists of dicts are the most common real-world data pattern.
# =============================================================================
