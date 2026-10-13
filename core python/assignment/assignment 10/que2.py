li=[10,40,50,20,60,90,80]
max=li[0]
min=li[0]
for i in range(1,len(li)):
    if(li[i]>max):
        max=li[i]
    elif(li[i]<min):
        min=li[i]
print(min)
print(max)
