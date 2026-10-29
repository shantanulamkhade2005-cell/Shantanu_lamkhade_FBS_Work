a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
for i in a:
    print(b,'-',a)
print("Missing in second set:", a - b)
print("Missing in first set:", b - a)