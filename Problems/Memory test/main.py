numbers = input().split()
answers = input().split()
result = bool

result_answers = bool
result_numbers = bool

for number in answers:
    if number not in numbers:
        result_answers = False
        break
    else:
        result_answers = True

for number in numbers:
    if number not in answers:
        result_numbers = False
        break
    else:
        result_numbers = True

if result_numbers is not result_answers or not result_numbers and not result_answers:
    result = False
    print(result)
else:
    result = True
    print(result)
