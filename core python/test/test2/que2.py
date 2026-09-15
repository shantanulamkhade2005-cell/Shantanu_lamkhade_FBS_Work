num=int(input('enter the no'))
temp=num
d1=temp%10
temp//=10
d2=temp%10
temp//=10
d3=temp%10
temp//=10
if(d3*2==d2  or  d3==d1/2 ):
    print('Yes you have done it')
else:
    print('please try next time')