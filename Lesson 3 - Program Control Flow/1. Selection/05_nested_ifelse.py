num = int(input("Enter value for num: "))

if num > 0:
    if num % 2 == 0:
       print(f"{num} is positive even number")
    else:
        print(f"{num} is a positive odd number")
else:
    print(f"{num} is a non-positive number.")
