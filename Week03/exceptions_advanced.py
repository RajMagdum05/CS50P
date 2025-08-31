# Week 3 - Exceptions Advanced
# ----------------------------
# Problem: How to keep asking user until they give correct input?

# Loop until valid integer
while True:
    try:
        x = int(input("Enter x: "))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")
        break  # Exit loop once valid input given

# -----------------------------------
# Using pass -> silently ignore error
while True:
    try:
        x = int(input("Enter x again: "))
        print(f"x is {x}")
        break
    except ValueError:
        pass  # Just ignore and ask again

# -----------------------------------
# Put logic in a function
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# main()

# -----------------------------------
# Catching Multiple Exceptions
try:
    x = int(input("Enter a non-zero integer: "))
    result = 10 / x
except ValueError:
    print("Invalid input! Must be an integer.")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Success! 10 divided by {x} is {result}")

# Another way: catching multiple exceptions together
try:
    x = int(input("Enter another non-zero integer: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as error:
    print(f"Oops! There was an error: {error}")
else:
    print(f"Success! 10 divided by {x} is {result}")
