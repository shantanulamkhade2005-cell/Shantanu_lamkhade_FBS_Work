#Write a function to which we pass a parameter and
#print the factors of a given number

def Factorial(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
n=int(input('enter the number: '))
Factorial(n)