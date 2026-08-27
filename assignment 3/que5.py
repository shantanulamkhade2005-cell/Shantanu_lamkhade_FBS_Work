a=int(input('enter the first angle'))
b=int(input('enter the second angle'))
c=int(input('enter the third angle'))
if(a==b and b==c and c==a):
    print('triangle is equilateral')
elif(a==b or b==c or c==a ):
    print('triangle is isosceles')
else:
    print('triangle is scalene')