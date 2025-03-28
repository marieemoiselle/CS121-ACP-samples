def main():
    try:
        numbers = [4, 6, 9]
        print(numbers[5])  
         # Raises IndexError
        text = None
        print(len(text))
        # Raises TypeError
    except IndexError as e:
        print("Array index out of bounds:", str(e))
    except TypeError as e:
        print("Null pointer exception:", str(e))
    except Exception as e:
        print("An unexpected exception occurred:", str(e))
    finally:
        print("The program continues...")

main()