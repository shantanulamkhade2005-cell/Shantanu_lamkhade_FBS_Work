for i in range(1,4):
    userid=int(input('enter the userid'))
    password=int(input('enter the password'))
    if(userid==123 and password==456):
        print('login successful')
        break
    else:
        print('login failed')
        print('please enter userid and password')
print('you have exceeded the limit of 3 attempts try after 24 hours')
