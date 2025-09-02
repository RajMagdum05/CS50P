# Week 3 - Exceptions Basics
# --------------------------
# Problem: Programs can crash due to errors.
# Example: user enters string when we expect a number.

# Types of errors:
# 1. Syntax Error -> mistake in code, must be fixed by programmer
# 2. Runtime Error -> happens while running program
# 3. Value Error -> when invalid value given (like string for int)

# Example: Syntax Error
# print("hello, world)   # missing quotation mark -> SyntaxError

# Example: Runtime Error
# x = int("cat")   # ValueError: invalid literal for int()

# -----------------------------------
# In Python try and except are ways of testing out user input before something goes wrong.
# ValueError with try-except
try:
    x = int(input("Enter x: "))
    print(f"x is {x}")
except ValueError:  # Only runs if error occurs
    print("x is not an integer")

# -----------------------------------
# Problem: If error happens, x is not defined (NameError)
try:
    x = int(input("Enter x: "))
except ValueError:
    print("x is not an integer")

# This will crash if ValueError happened earlier, because x was never set
# print(f"x is {x}")

# -----------------------------------
# Solution: use else with try-except
try:
    x = int(input("Enter x: "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")  # Runs only if no error

# prompt the user again to enter by using loop
while True:
    try:
        x = int(input("Enter x: "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
