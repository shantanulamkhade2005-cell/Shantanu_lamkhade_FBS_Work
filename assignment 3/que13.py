unit=int(input('enter the eletric unit'))
if(unit<=50):
    amount=unit*0.50
elif(unit<=150):
    amount=unit*0.75
elif(unit<=250):
    amount=unit*1.20
else:
    amount=unit*1.50
amount+=amount*0.20
print('total electricity bill is=',amount)
