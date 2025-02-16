import traceback

def main():
    try:
        numbers = [7, 14, 21]
        print(numbers[5])  # Raises IndexError
        text = None
        print(len(text))  # Raises TypeError
    except Exception:
        print("An error occurred:")
        traceback.print_exc()  # This prints all exception details

main()