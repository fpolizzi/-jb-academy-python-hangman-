import sys

scores = input().split()

score = 0
number_lose = 0

for letter in scores:
    if letter == "C":
        score = score + 1
    elif letter == "I":
        number_lose = number_lose + 1
        if number_lose == 3:
            print("Game over")
            print(score)
            sys.exit()

print("You won")
print(score)
