import math
base = 3
exponent = 5
square = 45
angle = 0.45

sq_result = math.sqrt(square)
pow_result = pow(5, 3)
sin_result = math.sin(angle)
cos_result = math.cos(angle)

print(f"{base} raised to {exponent} = {pow_result}") # 125
print(f"Sine of {angle} = {sin_result:.2f}") # 0.43
print(f"Cosine of {angle} = {cos_result:.2f}") # 0.90
print(f"Square root of {square} = {sq_result:.2f}") # 6.71