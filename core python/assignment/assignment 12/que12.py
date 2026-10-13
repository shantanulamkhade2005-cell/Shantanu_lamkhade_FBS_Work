text=input('enter the string:')
count=0
for i in range(len(text)):
    if text[i].islower():
        count+=1
print('Total no of lower case is:',count)