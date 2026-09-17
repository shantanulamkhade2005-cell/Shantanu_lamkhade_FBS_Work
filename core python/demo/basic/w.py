a=int(input('enter a number:'))
b=int(input('enter a number:'))
operation=input('enter the operation(+,-,*,/):')
if (operation=='+'):
    print('addition is:',a+b)
elif (operation=='-'):
    print('subtraction is:',a-b)
elif (operation=='*'):
    print('multiplication is:',a*b)
elif (operation=='/'):
    print('division is:',a/b)

color=input('enter the color:')
if(color=='red'):
    print('stop')
elif(color=='yellow'):
    print('ready')
elif(color=='green'):
    print('go')
else:
    print('invalid color')
     