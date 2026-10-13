di={1:'shantanu',2:'siddhesh',3:'shubham',4:'sachin'}
d2={'a':10,'b':20,'c':30}
sum=0
sum1=0
for key in di.keys():
    sum+=key
print("Sum of all key of dictionary:", sum)
for val in d2.values():
    sum1+=val
print("Sum of all values of dictionary:", sum1)