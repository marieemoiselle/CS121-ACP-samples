def fibonacci(n):
	if n <= 1:
		return n  
		# Base case: Fibonacci of 0 and 1 is the number itself
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)  
		# Recursive case: F(n) = F(n-1) + F(n-2)

num = 8
print("Fibonacci number at position", num, "is:", fibonacci(num))

# Output: 
# Fibonacci number at position 8 is: 21