def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age:", age)

try:
    check_age(-1)
except ValueError as e:
    print("An error occurred:", str(e))

# Call with a valid age
check_age(-1)