# CSV file -> comma separeted values
# so we need both student name and values which are separeted by comma

with open("students.csv") as file:  # dont need to write "r" bcz it is default
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        # row stores two values as a list and gives it by indexing

# so csv file -> by spliting it makes like two columns in a row
# Hermione   Gryffindor
# Harry      Gryffindor
# Ron        Gryffindor
# Draco      Slytherin

# we can
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# so it is hard to change specific part of the file 
# but easy to just update or change whole file

# so split returns 2 or more values and we can unpack it means assign that returned values to separate variables
# or store them in list

# We need to sort it
