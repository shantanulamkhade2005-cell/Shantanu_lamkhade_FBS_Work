def prime():
    n=int(input('enter the no'))
    for i in range(2,n):
        if(n%i==0):
            return False
            break
        else:
            return True
            break
res=prime()
print(res)

def pal():
    num=int(input('enter the number for palindrom no:'))
    temp=num
    while(num>0):
        d1=num%10
        num//=10
        d2=num%10
        num//=10
        d3=num%10
        num//=10
    reverse= (d1 * 100) + (d2 * 10) + d3
    print(reverse)
    if(reverse==temp):
        return True
    else:
        return False
b=pal()
print(b)


def strong():
    num=int(input('enter the no to state no is strong or not'))
    temp=num
    sum=0
    while(temp>0):
        d=temp%10
        temp//=10
        fact=1
        for i in range(1,d+1):
            fact=fact*i
        sum=sum+fact
    print(sum)
    if(sum==num):
        return True
    else:
        return False
c=strong()
print(c)

def amstrongNo():
    num=int(input('enter the no for amstrong no'))
    temp=num
    count=0
    while(temp>0):
        d=temp%10
        temp//=10
        count+=1
    sum=0
    temp=num
    while(temp>0):
        d=temp%10
        temp//=10
        sum=sum+(d**count)
    if(sum==num):
        return True
    else:
        return False
d=amstrongNo()
print(d)

def perfectNo():
    num=int(input('enter the no for perfect no:'))
    temp=num
    if(temp<=1):
        return False
    else:
        sum=0
        for i in range(1,num):
            if(num%i==0):
                sum+=i
            elif(sum==num):
                return True
                break
            else:
                return False  
                break
e=perfectNo()
print(e)