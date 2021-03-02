from itertools import combinations

file = open("numbers.txt", "r")

nums = []

for line in file:
    nums.append(int(line))

comb = combinations(nums, 3)

for i in list(comb):
    if(i[0] + i[1] + i[2] == 2020):
        print(i[0], i[1], i[2])
        print(i[0] * i[1] * i[2])
