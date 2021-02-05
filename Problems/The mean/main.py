number = int(input())

number_field = [int(n) for n in str(number)]
sum_field = sum(number_field)

print(sum_field / len(number_field))
