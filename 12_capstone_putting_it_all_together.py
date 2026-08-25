# =============================================================================
# CHAPTER 12 — CAPSTONE: PUTTING IT ALL TOGETHER
# =============================================================================
# This final chapter uses EVERYTHING from the course in one coherent program.
# Read through it and spot each concept as it appears.
#
# What we're building:
#   A small AI Session Manager — a tool that could realistically be used
#   to manage training sessions, track participants, log results,
#   and prepare a report.
#
# Concepts used:
#   ✓ Variables and data types
#   ✓ Lists and dictionaries
#   ✓ Conditionals
#   ✓ Loops
#   ✓ Functions
#   ✓ Classes and inheritance
#   ✓ Error handling
#   ✓ File handling
#   ✓ Modules and imports
#   ✓ JSON
#   ✓ API structure (simulated)
# =============================================================================

import json
import os
from datetime import datetime


# =============================================================================
# SECTION 1 — DATA MODELS (Classes)
# =============================================================================

class Participant:
    """Represents a session participant."""

    def __init__(self, name, role, department):
        # Variables + str type
        self.name         = name
        self.role         = role
        self.department   = department
        self.attended     = False    # bool
        self.quiz_score   = None     # None until quiz is taken
        self.notes        = []       # list — grows during the session

    def mark_attended(self):
        self.attended = True

    def record_score(self, score):
        """Record quiz score — must be 0-100."""
        # Error handling + conditionals
        if not isinstance(score, (int, float)):
            raise TypeError(f"Score must be a number, got {type(score).__name__}")
        if not (0 <= score <= 100):
            raise ValueError(f"Score must be between 0 and 100, got {score}")
        self.quiz_score = score

    def add_note(self, note):
        # List method
        self.notes.append(note)

    def get_result(self):
        """Return pass/fail/pending based on score."""
        # Conditionals
        if self.quiz_score is None:
            return "pending"
        elif self.quiz_score >= 70:
            return "pass"
        else:
            return "fail"

    def to_dict(self):
        """Convert to a dictionary — for JSON serialisation."""
        return {
            "name":       self.name,
            "role":       self.role,
            "department": self.department,
            "attended":   self.attended,
            "quiz_score": self.quiz_score,
            "result":     self.get_result(),
            "notes":      self.notes
        }

    def __repr__(self):
        return f"Participant({self.name}, {self.role})"


class Session:
    """Represents one training session."""

    def __init__(self, title, trainer, date=None):
        self.title        = title
        self.trainer      = trainer
        self.date         = date or datetime.now().strftime("%Y-%m-%d")
        self.participants = []       # list of Participant objects
        self.topics       = []
        self.is_complete  = False    # bool

    def add_participant(self, participant):
        """Add a participant — avoid duplicates."""
        # Check using a loop + conditional
        existing_names = [p.name for p in self.participants]
        if participant.name in existing_names:
            print(f"  ⚠ {participant.name} is already registered.")
            return
        self.participants.append(participant)
        print(f"  ✓ Registered: {participant.name}")

    def add_topic(self, topic):
        self.topics.append(topic)

    def get_participant(self, name):
        """Find a participant by name."""
        for p in self.participants:
            if p.name.lower() == name.lower():
                return p
        return None    # not found

    def get_statistics(self):
        """Calculate session statistics."""
        total       = len(self.participants)
        attended    = sum(1 for p in self.participants if p.attended)
        scored      = [p for p in self.participants if p.quiz_score is not None]
        passed      = [p for p in scored if p.get_result() == "pass"]

        # Avoid division by zero
        avg_score = round(sum(p.quiz_score for p in scored) / len(scored), 1) if scored else None
        pass_rate = round(len(passed) / len(scored) * 100, 1) if scored else None

        return {
            "total_registered": total,
            "total_attended":   attended,
            "attendance_rate":  round(attended / total * 100, 1) if total else 0,
            "avg_quiz_score":   avg_score,
            "pass_rate":        pass_rate,
            "passed":           len(passed),
            "failed":           len(scored) - len(passed),
            "pending":          total - len(scored)
        }

    def to_dict(self):
        return {
            "title":        self.title,
            "trainer":      self.trainer,
            "date":         self.date,
            "topics":       self.topics,
            "is_complete":  self.is_complete,
            "participants": [p.to_dict() for p in self.participants],
            "statistics":   self.get_statistics()
        }


# =============================================================================
# SECTION 2 — FUNCTIONS FOR THE WORKFLOW
# =============================================================================

def load_participants_from_file(filepath):
    """Load participant list from a JSON file. Returns a list of Participant objects."""
    if not os.path.exists(filepath):
        print(f"Participant file not found: {filepath}. Starting with an empty list.")
        return []

    try:
        with open(filepath, "r") as f:
            data = json.load(f)

        participants = []
        for item in data:
            p = Participant(item["name"], item["role"], item["department"])
            participants.append(p)

        print(f"Loaded {len(participants)} participants from {filepath}")
        return participants

    except json.JSONDecodeError as e:
        print(f"Error reading participant file: {e}")
        return []


def save_session_report(session, output_dir="/tmp"):
    """Save session data to a JSON report file."""
    filename  = f"session_{session.date}_{session.title.replace(' ', '_')}.json"
    filepath  = os.path.join(output_dir, filename)

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(session.to_dict(), f, indent=2)
        print(f"\n✓ Report saved: {filepath}")
        return filepath
    except (OSError, IOError) as e:
        print(f"Failed to save report: {e}")
        return None


def print_session_summary(session):
    """Print a human-readable summary to the console."""
    stats = session.get_statistics()
    sep   = "=" * 50

    print(f"\n{sep}")
    print(f"  SESSION SUMMARY")
    print(f"{sep}")
    print(f"  Title:    {session.title}")
    print(f"  Trainer:  {session.trainer}")
    print(f"  Date:     {session.date}")
    print(f"  Topics:   {', '.join(session.topics)}")
    print(f"{sep}")
    print(f"  Registered:       {stats['total_registered']}")
    print(f"  Attended:         {stats['total_attended']} ({stats['attendance_rate']}%)")

    if stats["avg_quiz_score"] is not None:
        print(f"  Avg Quiz Score:   {stats['avg_quiz_score']}/100")
        print(f"  Pass Rate:        {stats['pass_rate']}%")
        print(f"  Passed:           {stats['passed']}")
        print(f"  Failed:           {stats['failed']}")
        print(f"  Pending:          {stats['pending']}")

    print(f"\n  PARTICIPANTS:")
    for p in session.participants:
        score_str  = f"{p.quiz_score}/100" if p.quiz_score is not None else "no score"
        attended   = "✓" if p.attended else "✗"
        result     = p.get_result().upper()
        print(f"    {attended} {p.name:<15} {p.role:<20} {score_str:<10} [{result}]")

    print(f"{sep}\n")


def simulate_api_call(prompt, context):
    """
    Simulate a Claude API call for generating feedback.

    In a real implementation, this would:
    1. Build the request body (dict with model, messages, etc.)
    2. Send it via requests.post() to the Anthropic API
    3. Parse the JSON response and extract the text

    Here we return a canned response so the demo runs without an API key.
    """
    request_body = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 500,
        "system": "You are an AI training facilitator. Provide brief, constructive feedback.",
        "messages": [
            {"role": "user", "content": f"{prompt}\n\nContext: {json.dumps(context)}"}
        ]
    }

    # Simulated response:
    avg = context.get("avg_quiz_score", 0) or 0
    if avg >= 80:
        feedback = "Excellent session! Strong engagement and high scores suggest the material landed well. Consider adding an advanced follow-up module."
    elif avg >= 60:
        feedback = "Good progress. Most participants are on track. Recommend a short revision session on any topics where scores dipped below 70."
    else:
        feedback = "The group may need additional support. Consider breaking down the content into smaller chunks and adding more hands-on exercises before the next session."

    return feedback


# =============================================================================
# SECTION 3 — RUN THE PROGRAMME
# =============================================================================

def run_session_manager():
    """Main entry point — runs the full session management workflow."""

    print("\n" + "=" * 50)
    print("  AI SESSION MANAGER — DEMO RUN")
    print("=" * 50)

    # ------------------------------------------------------------------
    # STEP 1: Create the session
    # ------------------------------------------------------------------
    session = Session(
        title   = "Python Fundamentals for Leaders",
        trainer = "Intern (you!)"
    )

    session.add_topic("Variables & Data Types")
    session.add_topic("Loops & Conditionals")
    session.add_topic("Functions & Classes")
    session.add_topic("APIs & Claude")

    print(f"\nSession created: '{session.title}'")

    # ------------------------------------------------------------------
    # STEP 2: Register participants
    # ------------------------------------------------------------------
    print("\nRegistering participants...")

    participant_data = [
        ("Ananya Sharma",    "VP Engineering",   "Technology"),
        ("Dev Patel",        "Product Director", "Product"),
        ("Priya Nair",       "COO",              "Operations"),
        ("Rohan Mehta",      "Head of HR",       "People"),
        ("Sunita Kapoor",    "CFO",              "Finance"),
        ("Vikram Reddy",     "CTO",              "Technology"),
    ]

    for name, role, dept in participant_data:
        p = Participant(name, role, dept)
        session.add_participant(p)

    # Attempt to add a duplicate:
    session.add_participant(Participant("Priya Nair", "COO", "Operations"))

    # ------------------------------------------------------------------
    # STEP 3: Mark attendance (some are absent)
    # ------------------------------------------------------------------
    print("\nMarking attendance...")
    attended_names = ["Ananya Sharma", "Dev Patel", "Priya Nair", "Vikram Reddy", "Sunita Kapoor"]

    for name in attended_names:
        p = session.get_participant(name)
        if p:
            p.mark_attended()
            print(f"  ✓ {name} attended")
        else:
            print(f"  ✗ {name} not found")

    # ------------------------------------------------------------------
    # STEP 4: Record quiz scores
    # ------------------------------------------------------------------
    print("\nRecording quiz scores...")
    quiz_results = {
        "Ananya Sharma": 92,
        "Dev Patel":     78,
        "Priya Nair":    85,
        "Vikram Reddy":  95,
        "Sunita Kapoor": 61,
        # Rohan Mehta absent — no score
    }

    for name, score in quiz_results.items():
        p = session.get_participant(name)
        if p:
            try:
                p.record_score(score)
                p.add_note(f"Quiz completed on {session.date}")
                print(f"  {name}: {score}/100 [{p.get_result().upper()}]")
            except (ValueError, TypeError) as e:
                print(f"  Error recording score for {name}: {e}")

    # ------------------------------------------------------------------
    # STEP 5: Add notes for specific participants
    # ------------------------------------------------------------------
    priya = session.get_participant("Priya Nair")
    if priya:
        priya.add_note("Asked excellent questions about system prompts.")
        priya.add_note("Interested in advanced Claude Code usage.")

    sunita = session.get_participant("Sunita Kapoor")
    if sunita:
        sunita.add_note("Needs extra support with loops and functions.")
        sunita.add_note("Recommend one-to-one follow-up.")

    # ------------------------------------------------------------------
    # STEP 6: Mark session complete and print summary
    # ------------------------------------------------------------------
    session.is_complete = True
    print_session_summary(session)

    # ------------------------------------------------------------------
    # STEP 7: Generate AI feedback (simulated API call)
    # ------------------------------------------------------------------
    stats    = session.get_statistics()
    prompt   = "Based on the session statistics, provide brief feedback for the trainer."
    feedback = simulate_api_call(prompt, stats)

    print("AI-Generated Trainer Feedback:")
    print(f"  {feedback}\n")

    # ------------------------------------------------------------------
    # STEP 8: Save report to file
    # ------------------------------------------------------------------
    report_path = save_session_report(session, output_dir="/tmp/ai_sessions")

    if report_path:
        print(f"Report saved. You can open it to see all session data in JSON format.\n")

    return session


# =============================================================================
# ENTRY POINT
# =============================================================================
# This pattern — if __name__ == "__main__" — is standard in Python.
# It means: "only run this block if this file is being run directly,
# not if it's being imported by another file."
# This lets us safely import functions from this file without running the demo.

if __name__ == "__main__":
    completed_session = run_session_manager()

    # Demonstrate: access data programmatically after the run
    print("Post-run data access:")
    stats = completed_session.get_statistics()
    print(f"  Average score:   {stats['avg_quiz_score']}")
    print(f"  Pass rate:       {stats['pass_rate']}%")
    print(f"  Total attended:  {stats['total_attended']} / {stats['total_registered']}")


# =============================================================================
# WHAT TO LOOK FOR IN THIS FILE
# =============================================================================
#
#  Line ~20-30   → Classes (Participant, Session)
#  Line ~35      → __init__ constructor
#  Line ~40-50   → Attributes: strings, booleans, None, lists, dicts
#  Line ~55      → raise + error handling inside methods
#  Line ~70      → Conditionals in get_result()
#  Line ~80      → List comprehension / to_dict pattern
#  Line ~110     → for loop over a list of objects
#  Line ~125     → Function with try/except and file I/O
#  Line ~155     → json.dump (writing JSON)
#  Line ~165     → Formatted string output (f-strings)
#  Line ~185     → Simulated API request structure
#  Line ~230     → Main workflow function calling all the above
#  Line ~295     → if __name__ == "__main__" entry point pattern
#
# =============================================================================
