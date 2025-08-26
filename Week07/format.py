
#* user can enter input in any format like what programmer doesn't want
#* so before storing that we need to clean the data

name = input("What's your name: ").strip()

#* I want to store input as -> David Malan but what user enters malan, david then
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")