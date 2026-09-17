def prime(n,i):
    if(i>=n):
        return 0
    elif(n%i==0):
        return 1
    else:
        prime(n,i+1)
        return 0
n=int(input('enter the number '))
res=prime(n,i=2)
if(res==0):
    print(f'{n} is prime number')
else:
    print(f'{n} is not prime number')