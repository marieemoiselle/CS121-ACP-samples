def divide(dividend, divisor):
    try:
        result = dividend / divisor
        print("Result:", result)
    except ZeroDivisionError as e:
        print("An arithmetic exception occurred:", str(e))

if __name__ == "__main__":
    divide(100, 0)