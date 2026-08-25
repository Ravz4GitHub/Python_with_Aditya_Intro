# =============================================================================
# CHAPTER 07 — CLASSES & OBJECTS (OOP — Object-Oriented Programming)
# =============================================================================
# OOP is a way to organise code by grouping related DATA and BEHAVIOUR
# into a single unit called an OBJECT.
#
# Three core concepts:
#   - Class    → the blueprint (template / cookie cutter)
#   - Object   → an instance created from the blueprint (the actual cookie)
#   - Method   → a function that belongs to a class
#
# Without OOP: you'd have a dozen separate variables and loose functions
#              for every "thing" in your program — messy and hard to manage.
#
# With OOP: each "thing" carries its own data and knows how to act on it.
# =============================================================================


# -----------------------------------------------------------------------------
# 7.1  DEFINING A CLASS
# -----------------------------------------------------------------------------
# class keyword → class name (CapWords by convention) → colon

class Employee:
    """Represents an employee in the organisation."""

    # __init__ is the CONSTRUCTOR — it runs automatically when you
    # create a new object. It sets up the object's initial data.
    # 'self' always refers to the specific object being created.

    def __init__(self, name, role, level):
        self.name  = name     # attribute: belongs to this specific object
        self.role  = role
        self.level = level

    # A METHOD is a function defined inside a class.
    # The first parameter is always 'self' — it refers to the object.

    def introduce(self):
        """Print a short introduction."""
        print(f"Hi, I'm {self.name}, a {self.role} at Level {self.level}.")

    def get_discount(self):
        """Return the discount rate based on level."""
        if self.level >= 5:
            return 0.20
        elif self.level >= 3:
            return 0.10
        else:
            return 0.0


# -----------------------------------------------------------------------------
# 7.2  CREATING OBJECTS (instances)
# -----------------------------------------------------------------------------
# Call the class like a function — Python runs __init__ for you.

emp1 = Employee("Ananya", "Engineer",  6)
emp2 = Employee("Dev",    "Designer",  3)
emp3 = Employee("Priya",  "Manager",   5)

# Each is a separate object — same blueprint, different data.
emp1.introduce()
emp2.introduce()
emp3.introduce()

# Access attributes directly:
print(emp1.name)     # → "Ananya"
print(emp2.level)    # → 3
print(emp3.get_discount())   # → 0.20


# -----------------------------------------------------------------------------
# 7.3  MODIFYING ATTRIBUTES
# -----------------------------------------------------------------------------
print("\nBefore:", emp2.level)
emp2.level = 4              # direct attribute update
print("After promotion:", emp2.level)
emp2.introduce()            # the object reflects the updated data


# -----------------------------------------------------------------------------
# 7.4  ADDING MORE BEHAVIOUR
# -----------------------------------------------------------------------------
class BankAccount:
    """A simple bank account with deposit and withdrawal."""

    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
        self.history = []        # a list attribute — starts empty

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance  += amount
        self.history.append(f"+ {amount}")
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Balance: {self.balance}")
            return
        self.balance  -= amount
        self.history.append(f"- {amount}")
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_history(self):
        print(f"\nTransaction history for {self.owner}:")
        for entry in self.history:
            print("  ", entry)
        print(f"  Current balance: {self.balance}")


account1 = BankAccount("Priya", 1000)
account2 = BankAccount("Rohan")         # starts with 0 (default)

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)    # insufficient
account1.show_history()

account2.deposit(300)
account2.show_history()


# =============================================================================
# CHAPTER 7B — INHERITANCE
# =============================================================================
# Inheritance lets one class INHERIT attributes and methods from another.
# The child class gets everything the parent has, and can add/override more.
#
# This avoids repeating code. If Employee has 10 methods and Manager needs
# 9 of them plus 2 more, Manager just inherits Employee and adds 2 methods.
#
# Terminology:
#   Parent class / Base class / Superclass = the one being inherited FROM
#   Child class / Derived class / Subclass = the one inheriting
# =============================================================================

# -----------------------------------------------------------------------------
# 7.5  BASE CLASS
# -----------------------------------------------------------------------------
class Person:
    """Base class for all people in the system."""

    def __init__(self, name, email):
        self.name  = name
        self.email = email

    def introduce(self):
        print(f"Hi, I'm {self.name}. Contact: {self.email}")

    def send_email(self, subject):
        print(f"Sending '{subject}' to {self.email}")


# -----------------------------------------------------------------------------
# 7.6  CHILD CLASSES
# -----------------------------------------------------------------------------
class Staff(Person):
    """A staff member — inherits from Person."""

    def __init__(self, name, email, department, salary):
        super().__init__(name, email)   # call the parent's __init__
        self.department = department
        self.salary     = salary

    def get_payslip(self):
        print(f"Payslip for {self.name}: £{self.salary}/year")


class Manager(Staff):
    """A manager — inherits from Staff (which inherits from Person)."""

    def __init__(self, name, email, department, salary, team_size):
        super().__init__(name, email, department, salary)
        self.team_size = team_size
        self.reports   = []       # list of team members

    def add_report(self, staff_member):
        self.reports.append(staff_member)
        print(f"{staff_member.name} now reports to {self.name}.")

    def introduce(self):     # OVERRIDE the parent's introduce method
        print(f"Hi, I'm {self.name}, Manager of {self.department}. "
              f"I lead a team of {self.team_size}.")


# Test the hierarchy:
p  = Person("Guest",  "guest@example.com")
s  = Staff("Ananya",  "ananya@co.com",  "Engineering", 80000)
m  = Manager("Priya", "priya@co.com",   "Engineering", 120000, 8)

p.introduce()   # Person's introduce
s.introduce()   # Person's introduce (inherited — Staff didn't override it)
m.introduce()   # Manager's override

s.get_payslip()
m.get_payslip()   # inherited from Staff → Manager → (same method)

m.send_email("Team standup tomorrow")   # inherited from Person

m.add_report(s)


# -----------------------------------------------------------------------------
# 7.7  isinstance() and issubclass()
# -----------------------------------------------------------------------------
print("\nType checks:")
print(isinstance(m, Manager))   # True — m is a Manager
print(isinstance(m, Staff))     # True — Manager inherits from Staff
print(isinstance(m, Person))    # True — Staff inherits from Person
print(isinstance(m, str))       # False — not a string

print(issubclass(Manager, Staff))    # True
print(issubclass(Staff,   Person))   # True


# =============================================================================
# 7.8  HOW THIS RELATES TO CLAUDE
# =============================================================================
# Claude's codebase is built with classes and inheritance.
#
# Examples of what the real architecture looks like (simplified):
#
#   class BaseTool:
#       def run(self, input): ...
#
#   class WebSearch(BaseTool):
#       def run(self, query):
#           # search the web
#
#   class CodeExecutor(BaseTool):
#       def run(self, code):
#           # run Python code
#
# When you give Claude a tool, you're giving it an object — an instance
# of a class — and Claude calls .run() on it.
#
# The 'model' itself is an object. The 'tokenizer' is an object.
# Everything is organised this way.


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - Class = blueprint. Object = the actual thing built from it.
# - __init__ sets up an object's data when it's created.
# - self always refers to the specific object the method was called on.
# - Methods are just functions inside a class.
# - Inheritance: child gets all parent's attributes and methods for free.
# - super() calls the parent class's version of a method.
# - Override a method in a child class to change its behaviour.
# - isinstance() checks if an object is an instance of a class (or parent).
# =============================================================================
