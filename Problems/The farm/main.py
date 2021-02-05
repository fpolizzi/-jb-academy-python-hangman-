import sys

animal_list = ["chicken", "goat", "pig", "cow", "sheep"]
animal_price = [23, 678, 1296, 3848, 6769]

user_money = int(input())

int_max = 0
int_animal = 0

for i in animal_price:

    if i <= user_money:
        if i > int_max:
            int_max = i
            int_animal = int_animal + 1

if int_max == 0:
    print("None")
    sys.exit()
else:
    output_animal = animal_list[int_animal - 1]
    quantity = str((user_money // int_max))

    if output_animal == "sheep":
        print(str(quantity + " " + output_animal))
    elif quantity == "1":
        print(str(quantity + " " + output_animal))
    else:
        print(str(quantity + " " + output_animal + "s"))
