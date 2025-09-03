"""
Week 4 - Libraries
File 2: random_statistics.py

👉 Why use random and statistics?
- random: To simulate chance, randomness in games, lottery, sampling
- statistics: To calculate important measures (mean, median, mode)

👉 What they do?
- random.choice(seq), random.randint(a, b), random.shuffle(list)
- statistics.mean(), median(), mode()
"""

import random
import statistics

# Example 1: Random choice
fruits = ["apple", "banana", "cherry"]
print("Random fruit:", random.choice(fruits))

# Example 2: Random number
print("Random number between 1 and 10:", random.randint(1, 10))

# Example 3: Shuffle list
cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print("Shuffled cards:", cards)

# These are functions of module random so they can be accessed by ().
# Example 4: Statistics calculations
marks = [85, 90, 78, 92, 88, 90]
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Mode:", statistics.mode(marks))

"""
✅ Takeaways:
- random helps simulate unpredictability
- statistics helps analyze data
"""
# we can directly import specific function from module
from random import choice

coin = choice(["heads", "tails"])
print(coin)
