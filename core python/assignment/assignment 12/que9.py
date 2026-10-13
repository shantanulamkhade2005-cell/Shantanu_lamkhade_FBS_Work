text=input('enter the string:')
alpha=0
num=0
for i in range(len(text)):
    if(text[i].isdigit()):
        num+=1
    else:
        alpha+=1
print('the number of alphabets in the string is:',alpha)
print('the number of digits in the string is:',num)