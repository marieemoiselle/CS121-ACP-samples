# create a function definition
# note: if divisible by 3 = fizz
#       if divisible by 5 = buzz
#       if divisible by both 3 and 5 = fizzbuzz

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# implementation
fizz_buzz(15)
