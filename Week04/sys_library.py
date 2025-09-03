"""
Week 4 - Libraries
File 1: sys_library.py

👉 Why use sys?
- sys is a module that allows us to take arguments at the command line.
- argv is a list within the sys module that records what the user typed on the command line.
- The sys library helps interact with the Python interpreter.
- Mainly used for handling command-line arguments, exiting programs, 
  and accessing system-specific parameters.

👉 What it does?
- sys.argv → allows us to pass inputs when running program
- sys.exit() → exit program gracefully
- sys.argv[1:] → slice arguments (skip script name)

"""

import sys

print("Hello, My name is ", sys.argv[1])
# type -> python name.py David -> Hello, My name is David
# sys.argv[1] -> David is stored
# at sys.argv[0] -> name.py is stored

# what if user does not enter name or argument on command line -> IndexError
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
  
# can be improved as ->
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# can be improved as ->
# exit allows us to exit program if an error is introduced by an user.
# exit is built-in function of sys module.
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# Example 2: Handling multiple arguments
# what if -> python name.py Raj David Carter
# so to output all names ->
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv: # sys.argv is list
    print("hello, my name is", arg)

# but here as sys.argv[0] is name.py so it will also be printed at first
# use slice function 

if len(sys.argv) < 2:
  sys.exit("Too few Arguments")

for arg in sys.argv[1:]:
  print(f"Hello, my name is {arg}")
  
# Run: python sys_library.py Raj Magdum
print("All arguments:", sys.argv)  # prints list
print("Only names:", sys.argv[1:])  # slice to skip script name

# Example 3: Prevent IndexError
try:
    name = sys.argv[1]
    print(f"My name is {name}")
except IndexError:
    print("Error: Please provide at least one argument")

"""
✅ Takeaways:
- sys.argv is a list of command-line inputs
- Always check length before accessing indexes
- sys.exit(code) is used to stop program safely
"""

