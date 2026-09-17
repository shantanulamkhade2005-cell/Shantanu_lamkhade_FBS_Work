def fibo(n):
    a=0
    b=1
    for i in range(1,n+1):
        c=a+b
        a=b
        b=c
        print(a,end=" ")
n=int(input('enter the number for fibonency series:'))
fibo(n)
