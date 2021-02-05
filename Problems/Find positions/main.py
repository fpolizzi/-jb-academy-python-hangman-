sequence = input().split()
search_number = int(input())

if str(search_number) not in sequence:
    print("not found")
else:
    index = 0
    positions = ''

    for element in sequence:
        if int(element) == int(search_number):
            positions = positions + str(index) + ' '
        index = index + 1

    print(positions)
