import random
userid=input('enter the userid')
password=input('enter the password')
if(userid=='admin@123' and password=='123'):
    captcha=random.randint(1000,10000)
    print(captcha)
    cap=int(input('enter the captcha'))
    if(captcha==cap):
        print('successfuly login')
    else:
        print('invalid captcha')
else:
    print('invalid username and password')