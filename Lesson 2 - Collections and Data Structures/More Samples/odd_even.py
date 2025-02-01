n = int(input("Enter a number: "))
result = ["even" if i % 2 == 0 else "odd" for i in range(1, n+1)]
print(result)