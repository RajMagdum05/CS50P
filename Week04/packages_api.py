"""
Week 4 - Libraries
File 3: packages_apis.py

👉 Why use external packages?
- Python's built-in libraries are powerful, but sometimes we need extra tools.
- Example: fun text art (cowsay), web requests (requests).

👉 What is API?
- API = Application Programming Interface
- Allows programs to talk to each other
- Example: iTunes API → get song info
- so these cowsay, requests are APIs that are programmed generally and we can use it in our program directly just by calling it.

👉 What is JSON?
- Data format for communication
- Looks like Python dict but with strings
"""

# pip install requests
import cowsay
import requests
import json

# Example 1: Using cowsay package
cowsay.cow("Hello from Raj!")
cowsay.trex("Rawrrr!")

# Example 2: Fetching data from API
response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=Arijit+Singh")
data = response.json()

print("\nTop 5 songs of Arijit Singh from iTunes API:")
for song in data["results"]:
    print("-", song["trackName"])

# Example 3: JSON formatting
json_string = json.dumps(data, indent=2)  # indent for readability
print("\nFormatted JSON snippet:")
print(json_string[:500])  # print only part

"""
✅ Takeaways:
- External packages extend Python's power
- APIs allow us to fetch real-world data
- JSON is used for communication between servers and programs
"""

