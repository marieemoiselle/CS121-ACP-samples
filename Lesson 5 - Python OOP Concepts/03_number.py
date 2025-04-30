class Number:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def sign(self):
        if self.__value > 0:
            return "positive"
        elif self.__value < 0:
            return "negative"
        else:
            return "zero"

    @property
    def parity(self):
        return "even" if self.__value % 2 == 0 else "odd"

    @property
    def primality(self):
        if self.__value <= 1:
            return "neither"
        for i in range(2, int(abs(self.__value) ** 0.5) + 1):
            if self.__value % i == 0:
                return "composite"
        return "prime"

    def __str__(self):
        return (f"Value: {self.value}, Sign: {self.sign}, "
                f"Parity: {self.parity}, Primality: {self.primality}")


# Get input from the user
try:
    user_input = int(input("Enter an integer: "))
    num = Number(user_input)
    print(num)

    # Ask if user wants to change the value
    while True:
        response = input("\nChange the value? (y/n): ").strip().lower()
        if response == 'y':
            new_value = int(input("Enter new value: "))
            num.value = new_value
            print(num)
        elif response == 'n':
            print("Goodbye!")
            break
        else:
            print("Please enter 'y' or 'n'.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")