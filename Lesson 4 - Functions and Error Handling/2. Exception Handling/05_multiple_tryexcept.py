def main():
    try:
        numbers = [7, 14, 21]
        print(numbers[5])  # Raises IndexError
    except IndexError as e:
        print("Array index out of bounds:", str(e))
    
    try:
        text = None
        print(len(text))  # Raises TypeError
    except TypeError as e:
        print("Null pointer exception:", str(e))

main()