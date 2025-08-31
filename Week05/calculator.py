# Week 5 - Unit Tests
# --------------------
# In Python, we often need to test functions to ensure they behave correctly.
# There are 3 common ways:
#   1. Manual Testing (by running code and checking output)
#   2. Using "assert" keyword (quick way to validate assumptions)
#   3. Using "pytest" library (most efficient & powerful way)

# This file contains a simple function `square`
# which we will test using different methods in other files.

def square(n):
    """
    Function to return square of a number
    Example:
        square(3) -> 9
        square(-4) -> 16
    """
    return n * n


# Example of calling function directly
if __name__ == "__main__":
    print(square(2))   # 4
    print(square(5))   # 25
    print(square(-3))  # 9
