num=int(input('enter the no for perfect no'))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
        print(i,end="+")
print()
if(sum==num):
    print(f'{num} is perfect no')
else:
    print(f'{num} is not perfect no')