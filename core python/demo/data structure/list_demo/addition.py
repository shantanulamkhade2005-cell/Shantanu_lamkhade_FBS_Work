li=[10,20,30,40,50,60,70]
#method 1: Iterating values
sum=0
for ele in li:
    sum+=ele
print(sum)
sum=0
#method 2:
for i in range(0,len(li)):
    sum+=li[i]
print(sum)