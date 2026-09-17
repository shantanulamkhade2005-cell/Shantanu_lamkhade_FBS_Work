def reverse(n,s=0):
    if(n==0):
        return s
    else:
        d=n%10
        s=d+10*s
        return reverse(n//10,s)
n=int(input('enter the number'))
res=reverse(n)
print(f'after reverse the number of{n} becomes {res}')