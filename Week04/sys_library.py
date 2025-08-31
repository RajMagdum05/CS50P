"""
Week 4 - Libraries
File 1: sys_library.py

👉 Why use sys?
- The sys library helps interact with the Python interpreter.
- Mainly used for handling command-line arguments, exiting programs, 
  and accessing system-specific parameters.

👉 What it does?
- sys.argv → allows us to pass inputs when running program
- sys.exit() → exit program gracefully
- sys.argv[1:] → slice arguments (skip script name)

"""

import sys

# Example 1: Basic sys.argv usage
# Run this file from terminal: python sys_library.py Raj
if len(sys.argv) < 2:
    print("Usage: python sys_library.py [your name]")
    sys.exit(1)  # exit if no argument provided

print(f"Hello, {sys.argv[1]}!")

# Example 2: Handling multiple arguments
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
