# Testing using assert keyword
# ----------------------------
# "assert" is used to check if a condition is true.
# If it is false, program will stop with AssertionError.
# It is a quick and simple way to test small programs.

from calculator import square

# Valid test cases
assert square(2) == 4      # should pass
assert square(3) == 9      # should pass
assert square(-4) == 16    # should pass
assert square(0) == 0      # should pass

# Example of failing test (uncomment to see error)
# assert square(2) == 5   # this will raise AssertionError

print("All assert tests passed successfully ✅")

# Why use assert?
# - Good for quick checks
# - Immediately stops program if test fails
# - But not efficient for larger projects (pytest is better)
