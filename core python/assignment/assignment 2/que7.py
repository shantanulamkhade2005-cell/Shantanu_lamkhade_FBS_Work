num=int(input('enter the number:'))
d1=num%10
num //=10
d2=num%10
num //=10
d3=num%10
num //=10
total=d1+d2+d3
print(f'total of number is:{total}')