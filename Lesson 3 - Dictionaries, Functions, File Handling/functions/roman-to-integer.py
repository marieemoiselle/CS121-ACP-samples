def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    integer_value = 0
    prev_value = 0

    for numeral in reversed(roman):
        current_value = roman_values[numeral]
        if current_value < prev_value:
            integer_value -= current_value
        else:
            integer_value += current_value
        prev_value = current_value

    return integer_value


roman_numeral = input("Enter a Roman numeral: ").upper()

try:
    result = roman_to_integer(roman_numeral)
    print(f"The integer value of '{roman_numeral}' is: {result}")
except KeyError:
    print("Invalid Roman numeral entered.")
