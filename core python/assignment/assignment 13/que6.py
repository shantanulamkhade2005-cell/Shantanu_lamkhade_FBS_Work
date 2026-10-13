di={1:'shantanu',2:'siddhesh',3:'shubham',4:'sachin'}
d2={'a':10,'b':20,'c':30}
sum=1
sum1=1
for key in di.keys():
    sum*=key
print("Multiplication of all key of dictionary:", sum)
for val in d2.values():
    sum1*=val
print("Multiplication of all values of dictionary:", sum1)