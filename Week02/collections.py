# ============================================
# 📌 Week 2 - Collections (CS50P + My Notes)
# ============================================

# -----------------------------
# 1. Lists
# -----------------------------
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[0])         # apple
print(fruits[:2])        # ['apple', 'orange']
print(len(fruits))       # 4
print("apple" in fruits) # True

fruits.append("pineapple")
fruits.insert(0, "kiwi") # insert kiwi at index 0
fruits.sort() # sorts alphabetically
print("Sorted:", fruits)

# Iterating with index
for i in range(len(fruits)):
    print(i, fruits[i])

# Iterating directly
for fruit in fruits:
    print(fruit)


# -----------------------------
# 2. Sets
# -----------------------------
fruits_set = {"apple", "orange", "banana"}
fruits_set.add("pineapple")
print("Set:", fruits_set)

# Membership check
print("apple" in fruits_set) # True or False

# Iteration
for fruit in fruits_set:
    print(fruit)


# -----------------------------
# 3. Tuples
# -----------------------------
fruits_tuple = ("apple", "orange", "banana", "orange")
print(fruits_tuple[1])  # orange
print(fruits_tuple.count("orange"))  # 2


# -----------------------------
# 4. Dictionaries
# -----------------------------
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing"
}

print(capitals["India"])         # New Delhi
print(capitals.get("Japan"))     # None

capitals.update({"Germany": "Berlin"})
capitals.pop("China") # removes item
print(capitals)

for country, city in capitals.items():
    print(country, city)
# for only key -> capitals.keys()
# for only value -> capitals.values()
# use parathesis after the functions

# Hogwarts Example (CS50P)
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student, house in students.items():
    print(student, house)


# -----------------------------
# 5. List of Dictionaries
# -----------------------------
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


# -----------------------------
# 6. 2D Collections
# -----------------------------
fruits = ["apple", "banana"]
vegetables = ["tomato", "onion"]
proteins = ["eggs", "chicken"]

foods = [fruits, vegetables, proteins]

print(foods[0])        # ['apple', 'banana']
print(foods[0][1])     # banana

for category in foods:
    for item in category:
        print(item, end=" ")
    print()

