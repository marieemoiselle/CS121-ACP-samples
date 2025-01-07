def multiplier(n):
	return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(4))  # Output: 8
print(triple(5))  # Output: 15