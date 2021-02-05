column = int(input())
row = int(input())
moves = 0

if column in (1, 8) and row in (1, 8):
    moves = 3
elif column in (1, 8) or row in (1, 8):
    moves = 5
else:
    moves = 8

print(moves)
