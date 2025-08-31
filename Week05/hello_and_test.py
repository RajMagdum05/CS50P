# Return vs Print in Functions
# ----------------------------
# If a function prints a value, it cannot be easily tested.
# If a function RETURNS a value, we can test it using assert or pytest.

# Example 1: Print (not good for testing)
def hello_print(name):
    print(f"hello, {name}")

# Example 2: Return (better for testing)
def hello_return(name):
    return f"hello, {name}"

# Manual Testing
hello_print("Raj")   # prints: hello, Raj
print(hello_return("Raj"))  # prints: hello, Raj

# Assert Testing
assert hello_return("Raj") == "hello, Raj"
assert hello_return("CS50") == "hello, CS50"

print("Return-based function is easier to test ✅")

# Takeaway:
# - Use return instead of print in functions
# - Makes your code testable and reusable
