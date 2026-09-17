def revers(num,s=0):
    if(num==0):
        return s
    else:
        d=num%10
        s=d+10*s
        return revers(num//10,s) 
res=revers(num=123,s=0)
print(res)