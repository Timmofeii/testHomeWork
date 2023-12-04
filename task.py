coins = [0, 1, 0, 1, 1, 0]


import random
random_list = list()
count_zero = 0
count_one = 0
size = 10
for i in range(size):
    random_list.append(random.randint(0, 1))
    if random_list[i] == 0:
        count_zero += 1
    else:
        count_one += 1
result = min(count_zero, count_one)

print(result)
