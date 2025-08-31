# ========================================
# 📌 CS50P Week 0 – Strings
# ========================================

# ----------------------------------------
# 1. Basics
# ----------------------------------------
name = "bro Code"
# these are all operations or functions on strings

print(len(name))             # Length including spaces
print(name[0])               # Indexing: 'b'
print(name[-1])              # Negative index: last char
print(name[0:3])             # Slice: 'bro' it will not include cahr at index 3
print(name[::-1])            # Reverse string
# [::] -> if nothing means starts from first and end at last of the string and -1 for print from last

# ----------------------------------------
# 2. String Methods
# ----------------------------------------
print(name.upper())          # BRO CODE
print(name.lower())          # bro code
print(name.capitalize())     # Bro code , capitalize only char at index 0
print(name.title())          # Bro Code
print(name.strip())          # Remove whitespace

print(name.startswith("bro")) # True
print(name.endswith("e"))     # True
print(name.find("o"))         # First index of 'o' -> it returns index no.
print(name.rfind("o"))        # Last index of 'o'
print(name.replace("o", "a")) # bra Cade

print(name.isalpha())         # False (contains space) -> True or False
print("BroCode".isalpha())    # True
print("123".isdigit())        # True
print(" ".isspace())          # True

print(name.count("o"))        # Count occurrences of 'o'

# ----------------------------------------
# 3. String Operations
# ----------------------------------------
print(name * 3)              # Repeat string
print("Raj" + " " + "Magdum") # Concatenate strings

# ----------------------------------------
# 4. String Formatting
# ----------------------------------------
first = "Raj"
last = "Magdum"

print(f"Hello, {first} {last}") # f-string
print("Hello, {} {}".format(first, last)) # format()
print("Hello, " + first + " " + last)     # concatenation

# ----------------------------------------
# 5. Splitting & Joining
# ----------------------------------------
name = "Raj Magdum"
first, last = name.split(" ")
print(first, last)

words = ["CS50", "is", "fun"]
sentence = " ".join(words)
print(sentence)
# join words from list with " " between them

# ----------------------------------------
# 6. Slicing with slice() function
# ----------------------------------------
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice_obj = slice(7, -4) # we can use both positive and negative indexing at a time
print(website1[slice_obj]) # google
print(website2[slice_obj]) # wikipedia

# ----------------------------------------
# 7. Chaining Methods
# ----------------------------------------
name = input("Enter your name: ").strip().title()
print(f"Hello, {name}")


