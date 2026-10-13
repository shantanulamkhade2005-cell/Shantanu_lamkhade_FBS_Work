li=[10,40,50,84,60,90,80]
max=li[0]
smax=li[0]
for i in range(1,len(li)):
    if(li[i]>max):
        smax = max  
        max=li[i]
        # print(max)
    elif(li[i]>smax and li[i]!=max):
        smax=li[i]
print('second max=',smax)