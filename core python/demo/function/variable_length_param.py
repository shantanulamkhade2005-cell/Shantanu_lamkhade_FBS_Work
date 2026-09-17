def add(*num):
    sum=0
    for val in num:
        sum+=val
    return sum
n=int(input('enter the number:'))
for i in range(1,n):
    r=int(input('enter no:'))
    res=add(r)
print(res)