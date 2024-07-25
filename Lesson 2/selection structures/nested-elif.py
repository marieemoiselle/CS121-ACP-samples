num = int(input("Enter a value for num: "))
if num > 0:
    if num % 2 == 0:
        print("It is positive and even.")
    else:
        print("It is positive and odd.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")