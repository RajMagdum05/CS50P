# Week 1 - Functions
# Objectives:
# - Learn function basics
# - Use return values
# - Default arguments
# - Keyword arguments
# - *args and **kwargs

# --- Basic Function ---
def happy_birthday(name, age):
    print(f"Happy Birthday, {name}!")
    print(f"You are {age} years old.")
    print()

happy_birthday("Raj", 21)

# --- Function with Return ---
def create_name(first, last):
    return first.capitalize() + " " + last.capitalize()

print(create_name("raj", "magdum"))

# --- Default Arguments ---
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))          # default discount & tax
print(net_price(500, 0.1, 0))  # override defaults

# --- Keyword Arguments ---
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr", first="Raj", last="Magdum")

# --- *args (Arbitrary Positional Arguments) ---
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))  # any number of arguments

# Example: Display multiple names
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("Mr.", "Raj", "Magdum")

# --- **kwargs (Arbitrary Keyword Arguments) ---
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(city="Ich", state="MH", pincode="416143")

# --- Mixing *args and **kwargs ---
def shipping_table(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_table("Hello", "Raj", city="Ich", pincode="416143")
