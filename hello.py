# Testing strings

def main():
    name = input("Enter Uour name: ")
    hello(name)

def hello(to = "world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()

