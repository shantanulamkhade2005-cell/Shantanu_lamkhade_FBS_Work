tp=int(input('enter the tickit price:'))
for i in range(1,6):
    age=int(input('enter youe age'))
    if(age<12):
        final=tp*0.70
        print(f'for {age} age tickit price is {final}')
    elif(age>=60):
        final=tp*0.50
        print(f'for {age} age tickit price is {final}')
    else:
        print(f'for {age} age tickit price is {tp}')