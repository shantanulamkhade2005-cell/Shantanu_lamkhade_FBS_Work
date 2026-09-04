n=int(input('enter the range'))
d=int(input('enter the no which will divide the numbers'))
for i in range(1,n+1):
    if(i%d==0):
        print(i)