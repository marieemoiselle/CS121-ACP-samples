first_char = input("Enter First Character: ")
second_char = input("Enter Second Character: ")
size = int(input("Enter Size: "))

for i in range(1, size + 1):
    print("-" * (i - 1), end="")
    if i % 2 == 1:
        print(first_char)
    else:
        print(second_char)