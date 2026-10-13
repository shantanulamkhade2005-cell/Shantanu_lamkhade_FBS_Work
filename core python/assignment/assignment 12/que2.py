def remove_char(text, n):
    return text[:n] + text[n+1:]
text=input('enter the string:')
n=int(input('enter the index:'))
a=remove_char(text,n)
print('after removing the character at index',n,':',a)