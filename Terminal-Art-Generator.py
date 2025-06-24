import math

def triangle(length, symbol):
    """Prints a triangle of a given size s"""
    for row in range(1, length + 1):
        spaces = length - row
        num = row
        print(' ' * spaces + (symbol + ' ') * num)

def diamond(length, symbol):
    for row in range(1, length + 1):
        spaces = length - row
        print(' ' * spaces + (symbol + ' ') * row)
    
    for row in range(length - 1, 0, -1):
        spaces = length - row
        print(' ' * spaces + (symbol + ' ') * row)

def circle(length, symbol):
    for y in range(-length, length + 1):
        for x in range(-2 * length, 2 * length + 1):
            dist = math.sqrt((x / 2) ** 2 + y **2)
            if abs(dist - length) < 0.5:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        
        print()

def main():
    symbol = input("Enter a symbol: ")
    length = int(input("Enter the length of the pattern: "))
    
    choice = input("Enter the choice you wish to make of patterns: \n" \
    "1 for triangle, 2 for diamond, 3 for circle: ")

    if choice == '1':
        triangle(length, symbol)
    elif choice == '2':
        diamond(length, symbol)
    elif choice == '3':
        circle(length, symbol)
    else:
        print("Invalid choice. Please choose a valid option.")

main()