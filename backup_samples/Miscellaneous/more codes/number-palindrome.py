def is_palindrome(number):
    # Convert the number to a string to check its reverse
    original_str = str(number)
    reversed_str = original_str[::-1]
    
    if original_str == reversed_str:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# Example usage
number = int(input("Enter an integer: "))
result = is_palindrome(number)
print(result)
