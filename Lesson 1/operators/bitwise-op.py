num1 = 10    # Binary: 0000 1010
num2 = 6     # Binary: 0000 0110

result = num1 & num2     # Bitwise AND: 0000 0010 (2 in decimal)
print("AND Result:", result)

result = num1 | num2     # Bitwise OR: 0000 1110 (14 in decimal)
print("OR Result:", result)

result = num1 ^ num2     # Bitwise XOR: 0000 1100 (12 in decimal)
print("XOR Result:", result)

result = ~num1           # Bitwise complement: 1111 0101 (245 in decimal)
print("Complement Result:", result)

result = num1 << 2       # Left shift by 2: 0010 1000 (40 in decimal)
print("Left Shift Result:", result)

result = num2 >> 1       # Right shift by 1: 0000 0011 (3 in decimal)
print("Right Shift Result:", result)