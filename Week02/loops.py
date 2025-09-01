# ============================================
# 📌 Week 2 - Loops (CS50P + My Notes)
# ============================================

# -----------------------------
# 1. While Loops
# -----------------------------

# Example 1: simple counter
i = 0
while i < 3:
    print("meow")
    i += 1

# Example 2: validating input
name = input("Enter your name: ")
while name == "":
    print("Name can't be empty!")
    name = input("Enter your name: ")
print(f"Hello, {name}")

# Example 3: number validation
num = int(input("Enter a number between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is invalid.")
    num = int(input("Enter a number between 1-10: "))
print(f"Valid number: {num}")

# Example 4: infinite loop with break
while True:
    n = int(input("Enter n (positive): "))
    if n > 0:
        break
print(f"You entered {n}")


# -----------------------------
# 2. For Loops
# -----------------------------

# Basic examples
for i in range(3):
    print("meow") # prints meow 3 times and print comes with new line

# Using underscore when variable not needed
for _ in range(3):
    print("meow")

# Iterating with step
for x in range(1, 11, 2): # 1 included and goes upto 10 and iterates with 2 places i.e i+2
    print(x)   # if we dont put anything in 3rd place then it will increaments by 1 place

# Reverse iteration
for x in reversed(range(1, 11, 3)):
    print(x)
# reversed(range(1, 11)) -> so will print from 1 to 10 only but reversed i.e. 10 to 1
# range(11, 1) -> empty range not returns anything 
# range(11, 1, -1) -> so it starts with 11 and upto 2 and 1 is not included

# Looping over a string
credit_card = "1234-5678-9876-2341"
for digit in credit_card:
    print(digit, end=" ")
print()


# -----------------------------
# 3. Break and Continue
# -----------------------------

# Continue
for x in range(1, 21):
    if x == 13:
        continue
    print(x)

# Break
for x in range(1, 21):
    if x == 12:
        break
    print(x)


# -----------------------------
# 4. Nested Loops
# -----------------------------

for i in range(3):          # Outer loop = rows
    for j in range(5):      # Inner loop = columns
        print(j, end=" ")
    print()


# -----------------------------
# 5. Mario Example (CS50P)
# -----------------------------

def print_square(size):
    for i in range(size):  # each row
        for j in range(size):  # each column
            print("#", end="")
        print()  # new line after row


print_square(3)


# -----------------------------
# 6. List Comprehensions
# -----------------------------

# Basic usage
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# With condition
nums = [1, -2, 3, -4, 5]
positives = [n for n in nums if n > 0]
print("Positive numbers:", positives)

