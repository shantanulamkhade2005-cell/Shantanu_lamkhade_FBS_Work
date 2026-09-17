def sum(n):
    if(n>=0):
        return n+sum(n-1)
    return 0
n=6
res=sum(n)
print(res)