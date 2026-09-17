li=[10,70,30,60,90,80,82]
# for num in li:
#     for n in li:
#         if(num<n ):
#             break
#     else:
#         print(num)

max=li[0]
smax=0
for i in range(2,len(li)):
    if(li[i]>max):
        max=li[i]
    elif(li[i]>smax):
        smax=li[i]
print('second max=',smax)
 