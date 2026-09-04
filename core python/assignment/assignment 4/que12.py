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
    print(f'{num} is amstrong no')
else:
    print(f'{num} is not amstrong no')