num_a = int(input())
num_b = int(input())

num_sum = 0
num_iter = 0

for i in range(num_a, num_b + 1):
    if i % 3 == 0:
        num_sum = num_sum + i
        num_iter = num_iter + 1

print(num_sum / num_iter)
