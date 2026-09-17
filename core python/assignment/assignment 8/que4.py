def odd():
    n=int(input('enter the n:'))
    for i in range(1,n+1):
        if(i%2!=0):
            print(i,end=" ")
odd()