winner_list = []
n = int(input())
for _n in range(n):
    input_player = input()
    if input_player.endswith("win"):
        input_player.split()
        winner_list.append(input_player.split()[0])

print(winner_list)
print(len(winner_list))

