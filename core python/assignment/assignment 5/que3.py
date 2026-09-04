pa=int(input('enter the no of passangers:'))
co=int(input('enter the cost of ticket:'))
for i in range(1,pa+1):
    passenger=int(input('enter the age of passanger:'))
    if(passenger<12):
        print('the cost of ticket is:',co*0.70)
    elif(passenger>60):
        print('the cost of ticket is:',co*0.50)
    else:
        print('the cost of ticket is:',co)