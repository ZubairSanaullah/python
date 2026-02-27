def area (length, width):
    print(str(length * width) + " square units")
    return length * width

def main():
    house = area(20, 30)
    yard = area(50, 100)
    total = house + yard
    print(str(total) + " total square feet")

main()