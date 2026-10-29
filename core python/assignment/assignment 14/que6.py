a = [2, 3, 5, 7, 9, -10]
s = set(a)

a = list(s)
a.sort()

print(a[-1] * a[-2])
print(a[-1], a[-2])