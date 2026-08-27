angle1=int(input('enter the first angle'))
angle2=int(input('enter the second angle'))
angle3=int(input('enter the third angle'))
total=angle1+angle2+angle3
if(total==180):
    print('triangle is valid')
else:
    print('triangle is not valid')