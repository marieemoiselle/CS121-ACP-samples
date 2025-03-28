def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
num = 5
print(f"Fibonacci number at position {num}: {fibonacci(num)}")


# Output: 
# Fibonacci number at position 8 is: 21