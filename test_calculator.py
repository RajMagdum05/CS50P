from calculator import square





# instead of if else for checking test cases, use assert keyword
# if checks if this is true do this but assert gives nothing if true and Assertionerror if false
# it makes code shorter
# assert means it tells boldly that this it true 
# and if it is false then AsssertionError comes

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9

# so I want to see what is the reason for assertion error
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 cha square 4 nahi")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 cha square 9 nahi")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 cha square 4 nahi")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 cha square 9 nahi")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 cha square 0 nahi")

# so for each test we need to write diff try-except
# so here we get userfriendly output not just printed AssertionError

# so this is too big for testing means too much lines we have to write for testing small function
# pytest -> tool 3rd party library to test our code automatically
# for that -> pip install pytest
# then on CLI -> pytest test_calculator.py

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# so for each line it will shows our eroor
# F means failed and . means pass
# for each function in file it will test and give result 
# so it is best to make diff functions for specific type of input to get tested by multiple inputs
# as this fails at 2nd assert statement it will show that to us and then not checks furthur assert statements

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# it will give FF. means 1st function positive is failed, 2nd is failed and 3rd is correct

# now what if our input is str and not int then how should we Test it
# so if we enter any str like cat then it will give TypeError
# we should make function for it to handle that error
import pytest  # so first imoprt the pytest module
def test_str():
    with pytest.raises(TypeError):
        square("cat")
























def main():
    test_square()

# it gives AssertionError for specific line like here for square(3) == 9
if __name__ == "__main__":
    main() 