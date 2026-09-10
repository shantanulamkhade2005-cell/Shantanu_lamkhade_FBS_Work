
length = int(input('Enter length of wall: '))
height = int(input('Enter height of wall: '))
cost = int(input('Enter painting cost per sq.unit: '))

area = 4 * length * height
total_cost = area * cost

print('Area of four walls =', area)
print('Total cost of painting =', total_cost)
