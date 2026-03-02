# Infinite loop
# i = 3
# while i != 0:
#     print("Meow")


# Range 
# for _ in range(3):  # _ is a convention to indicate that the value is not used
#     print("Meow")

# Another way to do this
# print ("meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range (n):
#     print("meow")

# meow Function 

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")

main()