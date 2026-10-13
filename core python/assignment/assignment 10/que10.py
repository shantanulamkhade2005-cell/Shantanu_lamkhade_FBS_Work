li=[10,20,30,40,20,34,50,10,100]
i=0
n=int(input('enter the number you want to remove for list:'))
while(i<len(li)):
    if(li[i]==n):
        li.pop(i)
    else:
        i+=1
print('after remove number form list')
print(li)