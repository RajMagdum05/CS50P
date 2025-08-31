# Testing using pytest (Most Efficient Way)
# -----------------------------------------
# pytest is a popular testing framework in Python.
# It allows us to write multiple test functions and run them easily.
#
# To run:
#   Open terminal in VS Code and type: pytest test_calculator_pytest.py

from calculator import square
import pytest

def test_square_positive():
    assert square(2) == 4
    assert square(5) == 25

def test_square_negative():
    assert square(-3) == 9
    assert square(-5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_wrong_input():
    # Example: square("cat") should raise TypeError
    with pytest.raises(TypeError):
        square("cat")

# Why pytest is best?
# - Automatically finds and runs test functions
# - Gives detailed error reports
# - Supports testing exceptions, edge cases, and big projects
