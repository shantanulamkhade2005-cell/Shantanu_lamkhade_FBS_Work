str1=input('enter the string one:')
str2=input('enter the string two:')
str1count=0
str2count=0
for i in str1:
    str1count+=1
for j in str2:
    str2count+=1
if(str1count>str2count):
    print('string one is longer')
elif(str1count<str2count):
    print('string two is longer')
else:
    print('both strings are of equal length')