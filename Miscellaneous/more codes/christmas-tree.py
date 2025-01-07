num = 3
for i in range(1, num+1):
	print(" "*(2*num-i+3), end="")
	for j in range(1, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+3):
	print(" "*(2*num-i+1), end="")
	for j in range(-1, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+5):
	print(" "*(2*num-i), end="")
	for j in range(-2, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+3):
	print(" "*((2*num)), end="")
	print("* "*3)
