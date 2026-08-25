# =============================================================================
# CHAPTER 09 — MODULES & IMPORTS
# =============================================================================
# A module is simply a Python file that contains functions, classes,
# and variables you can use in other files.
#
# Instead of writing every tool yourself, you IMPORT them.
# Python comes with a huge standard library of modules.
# The wider Python community has published thousands more (packages).
#
# This is the foundation of how ALL real Python projects work —
# and it's exactly how Claude Code loads its tools.
# =============================================================================


# =============================================================================
# PART A — IMPORTING BUILT-IN MODULES
# =============================================================================

# -----------------------------------------------------------------------------
# 9.1  import — bring in an entire module
# -----------------------------------------------------------------------------
import math
import random
import os

# After importing, access things with a dot:
print(math.pi)                  # → 3.141592653589793
print(math.sqrt(144))           # → 12.0
print(math.ceil(4.2))           # → 5  (round up)
print(math.floor(4.9))          # → 4  (round down)
print(math.pow(2, 10))          # → 1024.0

print(random.randint(1, 100))   # random integer between 1 and 100 (inclusive)
print(random.choice(["a", "b", "c", "d"]))   # pick one at random

print(os.getcwd())              # current working directory


# -----------------------------------------------------------------------------
# 9.2  from module import name — import only what you need
# -----------------------------------------------------------------------------
from math import sqrt, pi
from random import choice, shuffle

# Now you can use these directly — no "math." prefix needed:
print(sqrt(256))      # → 16.0
print(pi)             # → 3.141592653589793

cards = ["Ace", "King", "Queen", "Jack", "10"]
shuffle(cards)        # shuffles the list in place
print(cards)
print(choice(cards))  # picks one


# -----------------------------------------------------------------------------
# 9.3  import as — give a module a shorter alias
# -----------------------------------------------------------------------------
# Very common when module names are long or clash with your own names.

import datetime as dt
import os.path as path

now = dt.datetime.now()
print("Current date/time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("Does /tmp exist?", path.exists("/tmp"))
print("Home dir:", path.expanduser("~"))


# =============================================================================
# PART B — KEY STANDARD LIBRARY MODULES
# =============================================================================

# -----------------------------------------------------------------------------
# 9.4  datetime — working with dates and times
# -----------------------------------------------------------------------------
from datetime import datetime, date, timedelta

today     = date.today()
now       = datetime.now()
yesterday = today - timedelta(days=1)
next_week = today + timedelta(days=7)

print("Today:", today)
print("Now:", now.strftime("%d/%m/%Y %H:%M"))   # formatted output
print("Yesterday:", yesterday)
print("Next week:", next_week)

# Parse a date string into a datetime object:
deadline = datetime.strptime("2025-12-31", "%Y-%m-%d")
print("Deadline:", deadline.date())

days_left = (deadline.date() - today).days
print("Days until deadline:", days_left)


# -----------------------------------------------------------------------------
# 9.5  json — working with JSON data
# -----------------------------------------------------------------------------
# JSON (JavaScript Object Notation) is the universal format for
# sending data between systems. APIs always use JSON.
# In Python, JSON looks almost identical to dicts and lists.

import json

# DICT → JSON string (serialisation)
user_data = {
    "name": "Priya",
    "role": "Manager",
    "skills": ["Python", "SQL", "Excel"],
    "active": True
}

json_string = json.dumps(user_data, indent=2)
print("JSON output:\n", json_string)

# JSON string → DICT (deserialisation)
raw_json = '{"model": "claude-3-5-sonnet", "temperature": 0.7}'
config   = json.loads(raw_json)
print("\nParsed config:", config)
print("Model:", config["model"])

# Read/write JSON files:
# with open("data.json", "w") as f:
#     json.dump(user_data, f, indent=2)   # write to file
#
# with open("data.json", "r") as f:
#     loaded = json.load(f)               # read from file


# -----------------------------------------------------------------------------
# 9.6  os — interacting with the operating system
# -----------------------------------------------------------------------------
import os

# File and directory operations:
print("\nCurrent dir:", os.getcwd())
print("Contents:", os.listdir("."))        # list files in current directory

# Environment variables (how secrets and configs are passed to programs):
# api_key = os.environ.get("ANTHROPIC_API_KEY", "not set")
# print("API Key:", api_key)

# Path operations:
home_dir  = os.path.expanduser("~")
full_path = os.path.join(home_dir, "documents", "report.pdf")
print("Full path:", full_path)
print("File extension:", os.path.splitext("report.pdf")[1])


# -----------------------------------------------------------------------------
# 9.7  sys — system-level information
# -----------------------------------------------------------------------------
import sys

print("\nPython version:", sys.version)
print("Platform:", sys.platform)
print("Script path:", sys.argv[0])         # the file being run

# sys.exit() would end the program here — not calling it in this demo


# -----------------------------------------------------------------------------
# 9.8  re — regular expressions (pattern matching in text)
# -----------------------------------------------------------------------------
# Regular expressions let you search for patterns in text.
# Very powerful — Claude uses them for parsing and extracting information.

import re

text = "Contact us at support@company.com or sales@company.co.uk"

# Find all email addresses:
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)
print("\nEmails found:", emails)

# Check if a string matches a pattern:
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

print(is_valid_email("priya@company.com"))   # → True
print(is_valid_email("not-an-email"))        # → False

# Replace text matching a pattern:
phone_text = "Call me at 0771-234-5678 or 0771.987.6543"
cleaned    = re.sub(r"[-.]", "", phone_text)   # replace - and . with nothing
print("Cleaned:", cleaned)


# =============================================================================
# PART C — INSTALLING & USING THIRD-PARTY PACKAGES
# =============================================================================

# -----------------------------------------------------------------------------
# 9.9  pip — Python's package installer
# -----------------------------------------------------------------------------
# Python's standard library is huge, but the community has built
# even more tools. You install them with pip (Package Installer for Python).
#
# Run in your terminal (NOT in a Python file):
#   pip install requests     ← install the requests library
#   pip install anthropic    ← install Anthropic's Claude SDK
#   pip install pandas       ← install data analysis library
#
# Then import normally in your Python code.


# -----------------------------------------------------------------------------
# 9.10 requests — making HTTP requests (fetching web data)
# -----------------------------------------------------------------------------
# requests is the most popular Python library. It's not built-in — install it:
# pip install requests
#
# Example of what it looks like (commented out to avoid network dependency):

# import requests
#
# response = requests.get("https://api.github.com")
# print("Status code:", response.status_code)   # 200 = success
# data = response.json()                         # parse JSON response
# print("GitHub API:", data["current_user_url"])
#
# # POST request with JSON body (like calling the Claude API):
# response = requests.post(
#     "https://api.anthropic.com/v1/messages",
#     headers={
#         "x-api-key": "your-api-key",
#         "content-type": "application/json",
#         "anthropic-version": "2023-06-01"
#     },
#     json={
#         "model": "claude-3-5-sonnet-20241022",
#         "max_tokens": 1024,
#         "messages": [{"role": "user", "content": "Hello, Claude!"}]
#     }
# )
# print(response.json()["content"][0]["text"])


# =============================================================================
# PART D — CREATING YOUR OWN MODULES
# =============================================================================

# -----------------------------------------------------------------------------
# 9.11 Making a module — it's just a .py file
# -----------------------------------------------------------------------------
# If you save functions in a file called helpers.py, you can import them:
#
#   # helpers.py
#   def clean_text(text):
#       return text.strip().lower()
#
#   def word_count(text):
#       return len(text.split())
#
# Then in another file:
#   from helpers import clean_text, word_count
#
# This is how real projects are structured — functionality split across
# many files, imported where needed.

# For demonstration, we'll define and use functions in the same file:
def clean_text(text):
    return text.strip().lower()

def word_count(text):
    return len(text.split())

sample = "  Hello World, how are you?  "
print("\nCleaned:", clean_text(sample))
print("Word count:", word_count(clean_text(sample)))


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - import loads a module so you can use its contents
# - from module import name lets you use it without the "module." prefix
# - import module as alias gives it a shorter name
# - Key built-in modules: math, random, os, datetime, json, re, sys
# - json is crucial — APIs send and receive JSON
# - pip installs third-party packages from the internet
# - Your own .py files ARE modules — import them the same way
# - Claude Code uses dozens of imported modules to do its work
# =============================================================================
