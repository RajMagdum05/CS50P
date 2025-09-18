# ========================================
# 📌 CS50P Week 0 – Basics
# ========================================

# ----------------------------------------
# 1. Printing in Python
# ----------------------------------------
print("Hello, World")       # Simple print
print("It's really good!!") # Strings can use single or double quotes

# Concatenation vs formatting
name = "Bro"
print("Hello " + name)        # Concatenation
print(f"Hello {name}")        # f-string (preferred)

# Multiple arguments in print
print("Hello,", name)         # Adds space automatically
print("Hello,", end="")       # Control line breaks
print(name)

# Escape sequences
print("hello, \"friend\"")    # Output: hello, "friend"
print('hello, "friend"')      # Alternative

# ----------------------------------------
# 2. Comments & Pseudocode
# ----------------------------------------
# Single-line comment
"""
Multiline comment
Good for notes or pseudocode
"""
# Pseudocode helps plan your program step by step.

# ----------------------------------------
# 3. Variables & Data Types
# ----------------------------------------
x = 10              # int
pi = 3.14           # float
name = "Raj"        # str
is_human = True     # bool

print(type(x))      # <class 'int'>
print(type(name))   # <class 'str'>

# Variables can be reassigned
x = x + 1  # or x += 1

# Concatenation works only on same type
# print("Age: " + 21) ❌ (error)
age = 21
print("Age: " + str(age))  # ✅ type casting

# ----------------------------------------
# 4. User Input
# ----------------------------------------
name = input("What's your name? ")
print(f"Hello, {name}")

age = int(input("How old are you? "))       # Cast to int
height = float(input("How tall are you? ")) # Cast to float

print(f"You are {age+1} years old")
print(f"You are {height} cm tall")

# ----------------------------------------
# 5. Multiple Assignment
# ----------------------------------------
a, b, c = 1, 2, 3
raj = prasad = parth = 20

# ----------------------------------------
# 6. Type Casting
# ----------------------------------------
x = 1
y = 2.0
z = "3"

print(str(x), int(y), int(z) * 3) # Casting between types

# ----------------------------------------
# 7. Numbers & Math Functions
# ----------------------------------------
import math
num = -3.7

print(round(num))       # Nearest integer
# print(round(4.5)) -> 4
# print(rount(5.5)) -> 6
# so it rounds to nearest even integer
print(math.ceil(num))   # Round up
print(math.floor(num))  # Round down
print(abs(num))         # Absolute value
print(pow(2, 3))        # 2^3 = 8
print(math.sqrt(16))    # 4.0

x, y, z = 10, 20, 30
print(max(x, y, z))     # 30
print(min(x, y, z))     # 10

# ----------------------------------------
# 8. Functions
# ----------------------------------------
def greet(name):  # parameter
    print(f"Hello, {name}!")

greet("Alice")    # argument

# Functions can have default values
def hello(to="world"):
    print(f"Hello, {to}")

hello("Raj")
hello()

# Return values
def square(n):
    return n * n

print("5 squared is", square(5))

# main() convention
def main():
    name = input("What's your name? ")
    hello(name)

# Call main
main()

