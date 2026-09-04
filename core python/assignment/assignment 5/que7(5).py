n=int(input('enter the value of n:'))
x=int(input('enter the value of x:'))
sum=0
sum1=0
sum2=0
for i in range(1,n+1):
    for j in range(1,i+1,2):
        if(i%2==0):
            sum1-=(x*i)/j
        else:
            sum2+=(x*i)/j
sum=sum1+sum2
print(sum)