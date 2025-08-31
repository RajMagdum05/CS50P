
# format specifiers = {value:flags}
# format value based on what flags are inserted

price1 = 30000.143768
price2 = -300000000.56

print(f"Price 1 is ${price1:.2f}") # to include only 2 decimal no.s
print(f"Price 2 is ${price2:.3f}") # for 3 decimal no.s

print(f"Price 1 is ${price1:10}") # it will make that integer value to 10 places
print(f"Price 2 is ${price2:4}") # it will not make shorter than existing length

print(f"Price 1 is ${price1:010}") # so it will add 0 before that no. to make total 10 spaces
print(f"Price 2 is ${price2:010}") # including - sign it will be 10 spaces

print(f"Price 1 is ${price1:<10}") # it will make total 10 spaces but add spaces more than value to the right at the end
print(f"Price 2 is ${price2:<14}")
# Left Justifier

print(f"Price 1 is ${price1:>10}") # same but it will add spaces to left at beginning
print(f"Price 2 is ${price2:>12}")
# Right Justifier

print(f"Price 1 is ${price1:^10}") # value is in center of total 10 places
print(f"Price 2 is ${price2:^10}")

print(f"Price 1 is ${price1:+}") # prints + before +ve value
print(f"Price 2 is ${price2:+}") # for -ve value it will print - only

print(f"Price 1 is ${price1:,}") # it will give , to thousands place
print(f"Price 1 is ${price1:,}")

# We can add multiple format specifiers in go also
print(f"Price 1 is ${price1:+,.2f}") # just give format specifiers one by one dont give , btw all
