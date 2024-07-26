def apply_operation(operation, x, y):
	return operation(x, y)

add = lambda x, y: x + y
subtract = lambda x, y: x - y

result1 = apply_operation(add, 5, 3)
print(result1)  # Output: 8

result2 = apply_operation(subtract, 5, 3)
print(result2)  # Output: 2