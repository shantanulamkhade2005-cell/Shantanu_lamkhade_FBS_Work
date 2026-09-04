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
if(sum==num):
    print(f'{num} is strong no')
else:
    print(f'{num} is not strong no')