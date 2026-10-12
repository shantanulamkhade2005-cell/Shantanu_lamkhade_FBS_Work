def Fatorial(n):
    if (n==0):
        return 1
    else:
        return n*Fatorial(n-1)
n=int(input('enter the number :'))
res=Fatorial(n)
print(res)