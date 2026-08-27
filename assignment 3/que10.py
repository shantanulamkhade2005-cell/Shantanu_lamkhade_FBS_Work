Gender=input('Enter your Gender(F/M)')
age=int(input('enter your age'))
if(Gender=='F'):
    if(age>=18):
        print('female is eligible to marry')
    else:
        print('female not eligible to marry')
else:
    if(age>=21):
        print('male is eligible to marry')
    else:
        print('male not eligible to marry')
