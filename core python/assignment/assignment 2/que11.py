money=int(input('enter the money:'))
d9=money//2000
d1=money%2000
a1=d1//500
d2=money%500
a2=d2//200
d3=money%200
a3=d3//100
d4=money%100
a4=d4//50
d5=money%50
a5=d5//20
d6=money%20
a6=d6//10
d7=money%10
print(f'notes of 2000: {d9}')
print(f'notes of 500: {a1}')
print(f'notes of 200: {a2}')
print(f'notes of 100: {a3}')
print(f'notes of 50: {a4}')
print(f'notes of 20: {a5}')
print(f'notes of 10: {a6}')