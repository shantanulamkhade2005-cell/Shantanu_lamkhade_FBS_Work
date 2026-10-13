def bubbleSort(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]

li=[50,40,30,20,10]
bubbleSort(li)
print(li)
print('second largest no is:',li[-2])