# for _ in range(3) means run this code for 3 times
# once our code is ended then it cant store what we had input so we need File I/O for that

# open -> used to open file
# first creates it then writes in it
# we need to -> code names.txt for that
# to remove names.txt -> rm names.txt

name = input("Enter name: ")

file = open("names.txt", "a") # file opens to variable file
file.write(f"{name}\n")
file.close() # we need to close file at end

## If i dont want to close the file
# with -> automate a closing of a file

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

## To read from a file
# first open file and read from it then print
with open("names.txt", "r") as file:
    lines = file.readlines() # lines is list it reads and store names from file to list lines

for line in lines:
    print(f"hello, {line.rstrip()}") 

# rstrip() strips off/ removes from right side of the each line
# we can
with open("names.txt") as file: # dont need to "r" bcz if we not, it is by-default read
    for line in file:
        print(f"hello, {line.rstrip()}")
# means we dont need to store first to list and then print
# we can just print as it is

## For sorting the names we have different methods
#1 list -> read and append names in list and print list
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        # we cant write sorted(file) here 

for name in sorted(names):
    print(f"hello, {name}")

#2 without making list
with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")
## We wanted to store Raj, DKTE
# CSV file -> comma separeted values
# in students.py