fav_color = input("Enter your favorite color: ")
value = int(input("Enter a value: "))
floating_point = float(input("Enter a floating-point value: "))
print("Favorite Color: ", fav_color)
print("Value entered: ", value)
print("Floating Point value: ", floating_point)

# using the map() function
num_list = list(map(int, input("Enter space-separated integers: ").split()))
print(num_list)

# multiple inputs
first_var, second_var = input("Enter two space-separated variables: ").split()
print(first_var)
print(second_var)
