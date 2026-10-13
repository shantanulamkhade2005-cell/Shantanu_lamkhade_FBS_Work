text=input('enter the string:')
count=0
for i in text:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count+=1
print('the number of vowels in the string is:',count)