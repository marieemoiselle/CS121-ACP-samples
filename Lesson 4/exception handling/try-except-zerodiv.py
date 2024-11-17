'''
Try this implementation without try-except, so that
you can see it for yourself.


def divide(dividend, divisor):
	result = dividend / divisor
	print("Result:", result)
	# print("An arithmetic exception occurred:", str(e))

if __name__ == "__main__":
	divide(100, 0)
	print("Hello world!")

'''

def divide(dividend, divisor):
	try:
		result = dividend / divisor
		print("Result:", result)
	except ZeroDivisionError as e:
		print("An arithmetic exception occurred:", str(e))

if __name__ == "__main__":
	divide(100, 3)
	divide(100, 0)
	print("Hello world!")
