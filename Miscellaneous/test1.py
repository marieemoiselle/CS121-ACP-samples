import math
expr1 = True and False
expr2 = not (False and True)
square_root = math.sqrt(25)

x = 45
y = 78

expr3 = ((x / 9) % 3 == 0 and (square_root <= y/2))
expr4 = not(not(expr2))


print(expr1)
print(expr2)
print(expr3)
print(expr4)