li=[1,2,3,4,5,6,7,8,9,10]
i=0
e=[]
o=[]
while(i<len(li)):
    if(li[i]%2==0):
        e.append(li[i])
    else:
        o.append(li[i])
    i+=1
print('even lisy:',e)
print('odd list:',o)