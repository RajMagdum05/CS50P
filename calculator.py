def square(n):
    return n * n
def main():
    x = int(input("What's x: "))
    print(f"x squared is {square(x)}")

if __name__ == "__main__":
    main() # This is to import safely this library to somewhere else

# now we need to check the function square actually works correctly in all cases.