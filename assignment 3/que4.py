a=int(input('enter the first side'))
b=int(input('enter the second side'))
c=int(input('enter the third side'))
if(a+b>c):
    if(a+c>b):
        if(b+c>a):
            print('trinagle is valid')
else:
    print('trinagle is not valid')