
#* regex - patterns, email is formatted correctly or not 

# email = input("Enter your Email: ").strip()
# #strip will remove whitespaces from right and left i.e beginning and ending of the input
 
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

#* so instead of applying logic for each corner case python has library for it
#* re -> regular expressions-> by using patterns it finds email is valid or not

### * re.search Function *
## search function in re module
#* re.search(pattern, string, flags=0)
# pattern -> @,  string -> email
# it returns True or False means it is there or not

import re
email = input("Enter email: ").strip() 
# these 2 lines will remain permanant

# if re.search("@", email, flags=0):
#     print("Valid")
# else:
#     print("Invalid")

# so to write regular expression perfect so every corner case should solved
# we use these functions or patterns
#* .   any character except a new line
#  *   0 or more repetitions
#* +   1 or more repetitions
#* ?   0 or 1 repetition
#* {m} m repetitions
#* {m,n} m-n repetitions

# if re.search(".+@.+", email):
# so now it only cares about left and right of @ it should be characters

# if re.search(".+@.+.edu", email): #any char, 1 or more time then @ then again any char one or more time then any char then edu

# so here . have special meaning in re so to use it as it is like literally . and not any char
#* use \ before it. then it will not consider it as re
# like f for formatting use r here which means raw string
# means i want to pass things exactly like this

# if re.search(r".+@.+\.edu", email):

# but this is also not fully correct

#* ^ -> starts with  ^The
#* $ -> ending with  end$

# if re.search(r"^.+@.+\.edu$", email):

#* [] set of caracters means these set of char are allowed
#* [^] these set of char are not allowed e.g. [^@] any char except @
# dont need to give "" to chars
# ("^[^@]+@[^@]+\.edu") -> it should start with any char except @ then @ then again same and then endwith .edu

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA_Z0-9_]+\.edu$", email):

#so instead of writing alphabets, numbers and _ is allowed and for other:
#* \d    decimal digit
#* \D    not a decimal digit
#* \s    whitespace characters
#* \S    not a whitespace character
#* \w    word character, as well as numbers and the underscore
#* \W    not a word character

# if re.search(r"^\w+@\w+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# if we want .edu, .com, .gov is allowed so we can group them using ()
#* | -> is used and not or

#* A|B     either A or B
#* (...)   a group
#* (?:...) non-capturing version

# if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
#     print("Valid")
# else:
#     print("Invalid")

#* (\w | \s) so word characters and white space is allowed so we can group them together

# for case sensitivity
# if user inputs everything uppercase using EDU then it might be problem
##* flags -> re.IGNORECASE
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")

#* within re.search function these flags can be used
#* re.IGNORECASE
#* re.MULTILINE
#* re.DOTALL

#* malan@cs50.harvard.edu for this ->
# group (\w+\.)?
if re.search(r"^\w+@(\w+\.)?\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

## other functions from module re -> re.match, re.fullmatch 