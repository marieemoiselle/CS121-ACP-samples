x = 5
y = 10

x_and_y = (x % 5 == 0 and y % 2 == 1)
x_or_y = (x % 5 == 0 or y % 2 == 1)
not_xy = not (x > y)

print(x_and_y)   # False
print(x_or_y)    # True
print(not_xy)    # True