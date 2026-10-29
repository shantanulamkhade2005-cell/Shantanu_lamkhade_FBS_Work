from itertools import combinations

a = [1, 2, 3, 4, 5, 6]
target = 10

for c in combinations(a, 3):
    if sum(c) == target:
        print(c)