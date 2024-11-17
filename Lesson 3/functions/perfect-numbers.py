def is_perfect_number(number):
    # check if a number is a perfect number
    if number <= 0:
        return False

    divisor_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    return divisor_sum == number


try:
    num = int(input("Enter a number: "))

    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
except ValueError:
    print("Please enter a valid integer.")
