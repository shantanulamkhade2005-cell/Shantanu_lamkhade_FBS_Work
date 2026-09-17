def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def check_armstrong(n):
    if n == 0:
        return True
        
    power = count_digits(n)
    original = n
    total_sum = 0
    
    while n > 0:
        digit = n % 10
        total_sum += digit ** power 
        n = n // 10
        
    return total_sum == original

num = int(input("Enter a number: "))

if check_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")