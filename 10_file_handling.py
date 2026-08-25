# =============================================================================
# CHAPTER 10 — FILE HANDLING
# =============================================================================
# Programs often need to read from and write to files.
# This is how programs store data that persists after they stop running,
# process documents, and communicate with other systems.
#
# Claude Code reads your project files, writes code, creates logs —
# all using the same file operations covered here.
# =============================================================================

import os
import json


# =============================================================================
# PART A — READING FILES
# =============================================================================

# -----------------------------------------------------------------------------
# 10.1  open() and the with statement
# -----------------------------------------------------------------------------
# open(path, mode) opens a file and returns a file object.
# Always use 'with' — it automatically closes the file when done,
# even if an error occurs.
#
# Common modes:
#   "r"  → read (default) — file must exist
#   "w"  → write — creates or OVERWRITES the file
#   "a"  → append — adds to the end of the file
#   "x"  → exclusive create — error if file already exists

# First, create a sample file to work with:
sample_path = "/tmp/sample.txt"

with open(sample_path, "w") as f:
    f.write("Line 1: Introduction to Python\n")
    f.write("Line 2: Variables and Data Types\n")
    f.write("Line 3: Functions and Classes\n")
    f.write("Line 4: Error Handling\n")
    f.write("Line 5: File Handling\n")

print("File created.")


# -----------------------------------------------------------------------------
# 10.2  Reading the entire file at once
# -----------------------------------------------------------------------------
with open(sample_path, "r") as f:
    content = f.read()     # reads the ENTIRE file as one string

print("Full content:")
print(content)


# -----------------------------------------------------------------------------
# 10.3  Reading line by line
# -----------------------------------------------------------------------------
with open(sample_path, "r") as f:
    lines = f.readlines()    # returns a list — one string per line

print("Line count:", len(lines))
print("First line:", lines[0].strip())   # .strip() removes the \n at the end


# -----------------------------------------------------------------------------
# 10.4  Iterating over lines (most memory-efficient)
# -----------------------------------------------------------------------------
# For large files, don't read all at once — iterate:

print("\nLine by line:")
with open(sample_path, "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"  {line_number}: {line.strip()}")


# =============================================================================
# PART B — WRITING FILES
# =============================================================================

# -----------------------------------------------------------------------------
# 10.5  Writing ("w" mode — overwrites if exists)
# -----------------------------------------------------------------------------
output_path = "/tmp/output.txt"

with open(output_path, "w") as f:
    f.write("Session report\n")
    f.write("=" * 30 + "\n")
    f.write("Participants: 12\n")
    f.write("Duration: 90 minutes\n")

print("Report written.")


# -----------------------------------------------------------------------------
# 10.6  Appending ("a" mode — adds without erasing)
# -----------------------------------------------------------------------------
with open(output_path, "a") as f:
    f.write("Topics covered: Python basics, Claude intro\n")
    f.write("Next session: Advanced prompting\n")

# Confirm by reading it back:
with open(output_path, "r") as f:
    print(f.read())


# -----------------------------------------------------------------------------
# 10.7  Writing multiple lines with writelines()
# -----------------------------------------------------------------------------
attendees = ["Priya\n", "Rohan\n", "Ananya\n", "Dev\n"]

attendees_path = "/tmp/attendees.txt"
with open(attendees_path, "w") as f:
    f.writelines(attendees)     # writes each item — no auto \n added

with open(attendees_path, "r") as f:
    print("Attendees:", f.read())


# =============================================================================
# PART C — JSON FILES
# =============================================================================
# JSON is the most common data format for configuration files and APIs.

# -----------------------------------------------------------------------------
# 10.8  Writing JSON to a file
# -----------------------------------------------------------------------------
config = {
    "project": "AI Training Programme",
    "sessions": 8,
    "participants": ["Priya", "Rohan", "Ananya"],
    "settings": {
        "model": "claude-3-5-sonnet",
        "max_tokens": 1024
    }
}

config_path = "/tmp/config.json"

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)     # indent=2 makes it human-readable

print("Config saved.")


# -----------------------------------------------------------------------------
# 10.9  Reading JSON from a file
# -----------------------------------------------------------------------------
with open(config_path, "r") as f:
    loaded_config = json.load(f)       # parses JSON back into a Python dict

print("Project:", loaded_config["project"])
print("Participants:", loaded_config["participants"])
print("Model:", loaded_config["settings"]["model"])


# =============================================================================
# PART D — FILE SYSTEM OPERATIONS
# =============================================================================

# -----------------------------------------------------------------------------
# 10.10  Checking if a file or directory exists
# -----------------------------------------------------------------------------
print("\nFile existence checks:")
print(os.path.exists(sample_path))          # True
print(os.path.exists("/nonexistent.txt"))    # False
print(os.path.isfile(sample_path))           # True — it's a file
print(os.path.isdir("/tmp"))                 # True — it's a directory


# -----------------------------------------------------------------------------
# 10.11  Getting file information
# -----------------------------------------------------------------------------
size  = os.path.getsize(sample_path)
print(f"File size: {size} bytes")

name  = os.path.basename(sample_path)
print(f"File name: {name}")                  # → sample.txt

folder = os.path.dirname(sample_path)
print(f"Directory: {folder}")                # → /tmp


# -----------------------------------------------------------------------------
# 10.12  Listing directory contents
# -----------------------------------------------------------------------------
tmp_files = os.listdir("/tmp")
print(f"\nFiles in /tmp (first 5): {tmp_files[:5]}")


# -----------------------------------------------------------------------------
# 10.13  Creating and deleting
# -----------------------------------------------------------------------------
new_dir = "/tmp/course_files"

if not os.path.exists(new_dir):
    os.makedirs(new_dir)              # creates directory (and parents if needed)
    print(f"Created: {new_dir}")

# Create a file inside it:
test_file = os.path.join(new_dir, "test.txt")
with open(test_file, "w") as f:
    f.write("Test content")

print(f"Contents of {new_dir}: {os.listdir(new_dir)}")

# Remove the file:
os.remove(test_file)

# Remove the empty directory:
os.rmdir(new_dir)

print("Cleaned up.")


# =============================================================================
# PART E — REAL-WORLD PATTERN: SAFE FILE OPERATIONS
# =============================================================================

# -----------------------------------------------------------------------------
# 10.14  Always wrap file operations in try/except
# -----------------------------------------------------------------------------
def read_config(filepath):
    """Read a JSON config file safely."""
    if not os.path.exists(filepath):
        print(f"Config not found: {filepath}. Using defaults.")
        return {}

    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        print(f"Config loaded from {filepath}")
        return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filepath}: {e}")
        return {}
    except PermissionError:
        print(f"No permission to read {filepath}")
        return {}


def save_results(filepath, results):
    """Save results to a JSON file, creating directories if needed."""
    try:
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, "w") as f:
            json.dump(results, f, indent=2)

        print(f"Results saved to {filepath}")
        return True
    except (OSError, IOError) as e:
        print(f"Failed to save results: {e}")
        return False


# Test them:
config_data = read_config("/tmp/config.json")
print("Sessions:", config_data.get("sessions", "unknown"))

save_results("/tmp/test_results.json", {
    "passed": 8,
    "failed": 2,
    "timestamp": "2025-01-15"
})


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - open(path, mode) opens a file — always use with open(...) as f
# - "r" = read, "w" = write (overwrites), "a" = append
# - f.read() → whole file as string. f.readlines() → list of lines.
# - Iterate directly over f for large files (memory efficient)
# - json.dump(obj, f) → write Python dict to JSON file
# - json.load(f) → read JSON file into Python dict
# - os.path.exists() checks before you read/delete
# - Always use try/except for file operations — files can be missing,
#   corrupt, or locked
# - Claude Code reads every file in your project the same way as above
# =============================================================================
