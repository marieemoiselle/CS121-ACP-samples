class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise CustomException("Custom exception occurred")
except CustomException as e:
    print("A custom exception occurred:", str(e))