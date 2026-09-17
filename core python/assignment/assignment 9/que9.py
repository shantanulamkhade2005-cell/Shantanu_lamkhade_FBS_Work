def power(m,n):
    if(n==0):
        return 1
    else:
        return m*power(m,n-1)

m=int(input('enter the m'))
n=int(input('enter the n'))
res=power(m,n)
print(f'{m} power of {n} is {res}')