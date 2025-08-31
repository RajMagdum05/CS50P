# Week 1 - Match Case
# Objectives:
# - Learn match (like switch in other languages)
# - Use multiple values in same case
# - Compare with if/elif/or approach

# --- Example 1: Days ---
def is_day(num):
    match num:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Not a valid day"

print(is_day(3))

# --- Example 2: Weekends and Weekdays ---
day = input("Enter a day: ").lower()

match day:
    case "sunday" | "saturday":
        print("Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case _:
        print("Invalid day")

# --- Alternative with if/or ---
if day in ["sunday", "saturday"]:
    print("Weekend (using if/or)")
elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Weekday (using if/or)")
else:
    print("Invalid day")
