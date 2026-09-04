n=int(input('enter the no of fibonacci series'))
a=0
b=1
i=1
while(i<=n):
    c=a+b
    print(a,end=" ")
    a=b
    b=c
    i+=1
   


