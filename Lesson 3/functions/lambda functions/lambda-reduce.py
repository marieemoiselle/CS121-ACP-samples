from functools import reduce
numbers = [2, 4, 6, 8, 10]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Output: 3840