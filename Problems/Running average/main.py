inp = input()
new_list = list(inp)
average_list = []

for x in new_list:
    if len(x) < len(new_list):
        y = (int(x) + int(x) + 1) / 2
        average_list.append(y)

average_list.pop()
print(average_list)
