n = int(input("Enter an upper bound: "))
fizzbuzz_list = []

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz_list.append("FizzBuzz")
    elif i % 3 == 0:
        fizzbuzz_list.append("Fizz")
    elif i % 5 == 0:
        fizzbuzz_list.append("Buzz")
    else:
        fizzbuzz_list.append(str(i))

# Print the results
print("\n".join(fizzbuzz_list))