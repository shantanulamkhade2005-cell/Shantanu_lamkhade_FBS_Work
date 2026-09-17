def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
            break
        else:
            return True
            break
n=int(input('enter the no'))
res=prime(n)
print(res)
def pal(num):
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
num=int(input('enter the number for palindrom no:'))
b=pal(num)
print(b)


def strong(num):
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
num=int(input('enter the no to state no is strong or not'))
c=strong(num)
print(c)

def amstrongNo(num):
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
num=int(input('enter the no for amstrong no'))
d=amstrongNo(num)
print(d)

def perfectNo(num):
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
num=int(input('enter the no for perfect no:'))
e=perfectNo(num)
print(e)