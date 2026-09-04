n=int(input('enter the number for range of n no for amstrong no'))
count=0
for i in range(1,n+1):
    temp=i
    count=0
    while(temp>0):  
        d=temp%10
        temp//=10
        count+=1
    sum=0
    temp=i
    while(temp>0):
        d=temp%10
        temp//=10
        sum=sum+(d**count)
    if(sum==i):
        print(i,end='  ')