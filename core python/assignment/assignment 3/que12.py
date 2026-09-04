num=int(input('enter the number for check palindrome or not'))
t=num
d1=num%10
num//=10
d2=num%10
num//=10
d3=num%10
num//=10
reverse= (d1 * 100) + (d2 * 10) + d3
print(reverse)
if(t==reverse):
    print('number is palindrome')
else:
    print('number is not palindrome')