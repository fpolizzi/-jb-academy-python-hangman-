height = int(input())
width = height * 2 - 1

for i in range(height):
    symbol = "#" * (2 * i + 1)
    print(symbol.center(width, ' '))
