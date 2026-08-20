#square root **0.5
a=float(input('enter the value of a:'))
b=float(input('enter the value of b:'))
c=float(input('enter the value of c:'))
#formula -b+/- sqrt(b**2-4ac)/2a
d=(b**2)-(4*a*c)
e=d**0.5
r1=(-b+e)/(2*a)
r2=(-b-e)/(2*a)
print(f'the roots of equation are {r1} and {r2}')
