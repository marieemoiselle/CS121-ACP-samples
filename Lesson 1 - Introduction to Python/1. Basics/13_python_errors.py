# Syntax Error
print("This is a string")
# Missing quotation mark

# Logical Error
num1 = 88
num2 = 89
num3 = 90
average = num1 + num2 + num3 / 3
print(f"Average: {average}")
# Average: 207.0 
# Missing parentheses -> (num1 + num2 + num3) / 3

# Runtime Error
value = 100
divisor = 0
quotient = value / divisor
print(f"Quotient: {quotient}")
# ZeroDivisionError: division by zero