sum_number = 0
square_result = 0

while True:
    number = int(input())

    sum_number = sum_number + number
    square_result = square_result + (number ** 2)

    if sum_number == 0 and square_result == 0:
        print(number)
        break
    elif sum_number == 0:
        print(square_result)
        break
