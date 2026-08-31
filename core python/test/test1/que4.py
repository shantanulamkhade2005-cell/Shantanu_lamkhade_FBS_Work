area=float(input('enter the area of one wall:'))
interior=float(input('enter the cost of interior wall:')) 
exterior=float(input('enter the cost of exterior wall:')) 
interior_wall=8
exterior_wall=7
i=interior_wall*area
c=i*interior
interior_paint=interior_wall*area*interior
exterior_paint=exterior_wall*area*exterior
print(f'cost of painting the interior walls is {interior_paint}')
print(f'cost of painting the exterior walls is {exterior_paint}')
print(c)