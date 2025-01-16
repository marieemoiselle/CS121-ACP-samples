def multiplier(n):
	return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(14))  
print(triple(90)) 