def number(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f'sum of n number is:{sum}')


def fact(n):
    sum=0
    fact=1
    for i in range(1,n+1):
        fact*=i
        sum+=fact
    print('sum of n factorial is:',sum)

def expo(n):
    sum=0
    for i in range(1,n+1):
        sum=i**i
    print(f'Sum of exponential is:{sum}')

n=int(input('enter the n:'))
number(n)
fact(n)
expo(n)