li=[10,20,30,40,20,34,50,10,100]
n=int(input('enter the number you want:'))
i=0
count=0
while(i<len(li)):
    if(li[i]==n):
        print(f'no is at {i} index')
        count+=1
    i+=1
print('no of count of no is:',count)
if(count==0):
    print('element not found')
