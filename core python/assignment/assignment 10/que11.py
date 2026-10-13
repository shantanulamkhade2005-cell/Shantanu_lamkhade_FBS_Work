li=[1,2,3,4,5,6,7,8,9,10]
i=0
m=int(input('enter the m :'))
n=int(input('enter the n'))
for i in range(0,len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i],end=" ")
        