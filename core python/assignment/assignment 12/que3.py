str1=input('enter the string one:')
str2=input('enter the string two:')
a="".join(sorted(str1))
b="".join(sorted(str2))
print(a,b)
if(a==b):
    print('the strings are anagrams')
else:
    print('the strings are not anagrams')
