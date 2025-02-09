first_char = input("First character: ")
second_char = input("Second character: ")
size = int(input("Enter size: "))

for i in range(1, size + 1):
    print("-" * (i - 1), end="")
    if i % 2 == 1:
        print(first_char)
    else:
        print(second_char)