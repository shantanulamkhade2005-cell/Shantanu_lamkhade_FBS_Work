r=float(input('enter the radius '))
l=float(input('enter the length'))
b=float(input('enter the breadth'))
area_rectangle=l*b
area_semicir=0.5*3.14*r**2
perimeter_rectangle=2*(l+b)
perimeter_semicir=3.14*r
total_area=area_rectangle+area_semicir
total_perimeter=perimeter_rectangle+perimeter_semicir
print(f'area of the give figure is {total_area}')
print(f'perimeter of give figure is {total_perimeter}')