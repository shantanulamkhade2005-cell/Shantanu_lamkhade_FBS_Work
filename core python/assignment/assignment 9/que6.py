def fibo(n,b,a):
    if(n==0):
        return 0
    else:
        c=a+b
        print(a,end=" ")
        fibo(n-1,b=a,a=c)
n=int(input('enter the n'))
fibo(n,b=1,a=0)
    
    
