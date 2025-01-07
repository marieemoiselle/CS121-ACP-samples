def fibonacci_squares(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    squares = [x ** 2 for x in fib]
    
    for square in squares:
        print(square)

# Output the squares of the first 20 Fibonacci numbers
fibonacci_squares(20)