start = 1
end = 10
numbers = list(range(start, end + 1))
squares = [num ** 2 for num in numbers]
cubes = [num ** 3 for num in numbers]

print("Numbers: ", numbers)
print("Squares: ", squares)
print("Cubes:   ", cubes)