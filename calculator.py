# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

# A better way to do this is to convert the input to an integer immediately:

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

# Floating-point numbers:

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f'{z:,}')