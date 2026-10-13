text=input('enter the string:')
t=list(text)
t[0],t[len(t)-1] = t[len(t)-1],t[0]
print('after swapping the first and last character:',"".join(t))