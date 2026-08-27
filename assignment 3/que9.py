math=int(input('enter th math marks'))
science=int(input('enter the science marks'))
history=int(input('enter the history marks'))
english=int(input('enter the english marks'))
marathi=int(input('enter the marathi marks'))
t=math+science+history+english+marathi
total=(t/500)*100
if(total>=90):
    print('First class')
elif(total>=70):
    print('second class')
elif(total>=50):
    print('third class')
elif(total>=35):
    print('pass')
else:
    print('fail')