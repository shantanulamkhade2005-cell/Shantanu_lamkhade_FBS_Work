
for i in range(90, -1, -10):
    row = list(range(i + 1, i + 11))
    

    if i % 20 != 0:
        row = row[::-1]

    print(*(f"{num:3}" for num in row))

