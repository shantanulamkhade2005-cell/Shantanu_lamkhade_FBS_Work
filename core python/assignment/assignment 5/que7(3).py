n=int(input('enter the n number value'))
sum=0
for i in range(1,n+1):
    sum+=(2**i)-1
print(sum)
