num=int(input('enter the number'))
temp=num
rev=0
while(temp>0):
    d=temp%10
    temp//=10
    rev=rev*10+d
print(rev)
if(num==rev):
    print('no is pallindrom')
else:
    print('no is not pallindrom')