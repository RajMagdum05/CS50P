# Week 1 - Conditionals
# Objectives:
# - Understand if, elif, else
# - Use comparison operators, logical operators
# - Use modulo for parity (even/odd)
# - Write pythonic one-liners

# --- Comparison Operators ---
# >, <, >=, <=, == (equals), != (not equal)

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# --- Logical Operators ---
# and, or, not

score = int(input("Enter your score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# --- More Pythonic Range Checking ---
if 90 <= score <= 100:
    print("Pythonic: Grade A")

# --- Modulo Operator ---
# Check parity (even/odd)
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# --- Pythonic Parity Function ---
def is_even(n):
    return n % 2 == 0

print("Even" if is_even(n) else "Odd")

# --- Conditional Expressions (Ternary Operator) ---
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Child"
print(status)

# --- Example: Validate Username ---
username = input("Enter username: ")

if len(username) > 12:
    print("Too long!")
elif " " in username:
    print("No spaces allowed!")
elif any(char.isdigit() for char in username):
    print("No digits allowed!")
else:
    print(f"Welcome, {username}")
