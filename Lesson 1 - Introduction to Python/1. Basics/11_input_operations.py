# integer
age = int(input("Enter your age: "))
print("Your age is:", age)


# string
name = input("Enter your name: ")
print("Your name is:", name)

# float
float_var = float(input("Enter a floating-point number: "))
print(float_var)

# boolean
bool_var = bool(input("Enter a boolean value (True/False): "))
print(bool_var)

# integers list
num_list = list(map(int, input("Enter space-separated integers: ").split()))
print(num_list)

# multiple inputs
var1, var2 = input("Enter two space-separated variables: ").split()
print(var1)
print(var2)
