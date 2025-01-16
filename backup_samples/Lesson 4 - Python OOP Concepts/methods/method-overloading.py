#Method overloading - multiple methods with the same name, but different parameter list

def get_sum(x, y = 5):
    return x + y

sum = get_sum(4, 12)
print(f"Sum: {sum}")