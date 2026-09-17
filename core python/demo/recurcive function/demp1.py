def series(n):
    if(n<=0):
        return 0
    else:
        return n+series(n-1)
n=5
res=series(n)
print(res)



