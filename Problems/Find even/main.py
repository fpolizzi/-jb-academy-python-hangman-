in_number = int(input())
counter = 1

if 0 < in_number <= 200:
    while counter < in_number:
        if counter % 2 == 0:
            print(counter)

        counter = counter + 1
