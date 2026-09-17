num=int(input('enter the no'))
temp=num
count=0
while(temp>0):
    count+=1
    temp//=10
temp=num
sum=0
while(temp>0):
    d=temp%10
    temp//=10
    sum=sum+(d**count)
if(sum==num):
    print(f'{num} is amstrong no')
else:
    print(f'{num} is not amstrong no')