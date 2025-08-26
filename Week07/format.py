
#* user can enter input in any format like what programmer doesn't want
#* so before storing that we need to clean the data

import re
name = input("What's your name: ").strip()

#* I want to store input as -> David Malan but what user enters malan, david then
# malan, david -> david malan
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

# malan,david -> david malan
#* so we can use re bcz trail and error all the possibilties will not be effective

#* so re.search returns either it is in string i.e. here name or not i.e. True or False
matches = re.search(r"^(.+),(.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"Hello, {name}")

##* So use () to capture processes and it returns to matches
#* last = matches.group(1), first = matches.group(2)
#* so here, first () assigns to first variable i.e last and vicevarsa
#* so it starts with 1 and not 0

# we can
if matches:
    name = matches.group(2) + " " + matches.group(1)
#* so here it is group bcz it is single implementation here
# we can make it like re.search(r"^(.+), *(.+)$")
# now here if there is space or spaces after , then also it works and if no , then also works

# to make it more compact ->
if matches := re.search(r"^(.+), *(.+)$"):
    name = f"{matches.group(2)} {matches.group(1)}"
#* := walrus operator
#* lets us combine assigning value and ask boolean que at the same time in one line


###* So, final one is use ( ) to capture values from re.search function and store to different variables or one as a list
#* matches.groups() then to diff variables
#* or matches.group(1) like this to use it directly and it starts with 1 and not 0
