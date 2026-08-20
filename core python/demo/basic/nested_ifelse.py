gender=input('enter your gender')
age=int(input('enter your age'))
if(gender=='F' and gender=='f'):
    if(age>=18):
        print('girl is eligible for marriage')
    else:
        print('girl is not eligible')
else:
    if(age>=21):
        print('boy is eligible for marriage ')
    else:
        print('boy is not eligible')
