def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print(False)
            break
        else:
            print(True)
            break
n=int(input('enter the no'))
prime(n)

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
        print(True)
    else:
        print(False)
num=int(input('enter the number for palindrom no:'))
pal(num)

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
        print(True)
    else:
        print(False)
num=int(input('enter the no to state no is strong or not'))
strong(num)


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
        print(True)
    else:
        print(False)
num=int(input('enter the no for amstrong no'))
amstrongNo(num)


def perfectNo(num):
    temp=num
    if(temp<=1):
        print(False)
    else:
        sum=0
        for i in range(1,num):
            if(num%i==0):
                sum+=i
            elif(sum==num):
                print(True)
                break
            else:
                print(False)  
                break
num=int(input('enter the no for perfect no:'))
perfectNo(num)