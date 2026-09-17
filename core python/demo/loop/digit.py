num=int(input('enter th no'))
temp=num
while(temp>0):
    d=temp%10
    temp//=10
    print(d,end='')
