from functools import reduce
numbers = [7, 14, 21, 28, 35]
product = reduce(lambda x, y: x * y, numbers)
print(product)  

# Output: 2016840