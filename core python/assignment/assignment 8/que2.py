def circle(r):
    area=(3.14)*r**2
    return area
r=int(input('enter the radius of circle:'))
res=circle(r)
print(f'area of circle is:{res}')