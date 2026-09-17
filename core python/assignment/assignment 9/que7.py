def sumOfdigit(n):
    if(n==0):
        return 0
    else:
        d=n%10
        return d+sumOfdigit(n//10)
n=int(input('enter the number'))
res=sumOfdigit(n)
print(res)