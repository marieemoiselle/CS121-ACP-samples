def check_age(age):
	if age < 0:
		raise ValueError("Age cannot be negative")
	print("Age:", age)

try:
	check_age(-2)
except ValueError as e:
	print("An illegal argument exception occurred:", str(e))