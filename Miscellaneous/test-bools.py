x = 7
y = 14

test_expr = (x < y)
test_and = (x % 7 == 0 and y % 2 == 1)
test_or = (x % 7 == 0 or y % 2 == 1)
test_not = not (x < y)

print("Showing the results: ")
print(f"test_expr = {test_expr}") # True
print(f"test_and = {test_and}") # False
print(f"test_or = {test_or}") # True
print(f"test_not = {test_not}") # False