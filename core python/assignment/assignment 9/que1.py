def factorial(n):
    if(n<=1):
        return 1
    return n*factorial(n-1)

def sum_of_series(n):
    if n <= 1:
        return factorial(1)
    return factorial(n) + sum_of_series(n - 1)

n = int(input('enter the number'))
total_sum = sum_of_series(n)
print(f"The sum of the series up to {n}! is: {total_sum}")