def digit():
    n=int(input('enter the n no:'))
    sum=0
    while(n>0):
        d=n%10
        n//=10
        sum+=d
    print(sum)
digit()