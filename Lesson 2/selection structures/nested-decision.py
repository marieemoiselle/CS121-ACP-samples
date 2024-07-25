num = int(input("Enter a value for num: "))

if num > 0:
	if num < 10:
		print("The number is less than 10.")
	else:
		print("The number is greater than 10.")
else:
	if num < 0:
		print("The number is a negative number.")
	else:
		print("The number is zero.")