#num=int(input('enter the num'))
#for i in range(2,num):
 #   if(num%i==0):
     #   print(f'{num} is not prime no')
    #    break
#else:
 #   print(f'{num} is prime no')

n=int(input('enter the no'))
for num in range(2,n+1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num,end=" ")

    



