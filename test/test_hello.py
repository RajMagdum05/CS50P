from hello import hello
  
  
def test_default():
    assert hello() == "hello, world"
  
  
def test_argument():
    assert hello("David") == "hello, David"

# we need to create __init__.py file so pytest will allow us to test all the files in this folder test at one command
# pytest test will run all files and there functions each line at one command
# so it will give like 2 passed means 2 files, if one of the statement from one function from one file is wrong it will give failed to that whole file 
# 1st passed for test_hello.py and 2nd passed for __init__.py