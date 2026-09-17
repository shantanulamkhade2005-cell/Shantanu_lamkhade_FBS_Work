def rev(n):
    r=0
    while(n>0):
        d=n%10
        r=(r*10)+d
        n//=10
    print(r)
n=int(input('enter the number:'))
rev(n)