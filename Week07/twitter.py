
#* Extracting specific info from input 
#* like extracting username from url

import re
url = input("URL: ").strip()

#1
# username = url.replace("https://twitter.com/", "")
#print(username)
# but what if user types just twitter.com or forget s in https and many other cornor cases

#* removeprefix is function of str -> removes beginning of a string

#* so re lets us express patterns much more precisely
#* we will struggle using string methods and other logic to solve all the cornor cases but using re it will be easy to solve it

#* ( ) -> to group patterns and also to capture info

###* re.sub -> substitute a pattern with something else
# re.sub(pattern, replacement, string, count=0, flags=0)

# username = re.sub("https://twitter.com/", "", url)
# the code is not idle

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

###* using re.search method

matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    username = matches.group(3)
print(username)




























print(username)
