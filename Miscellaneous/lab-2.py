def intToRoman(num: int) -> str:
    symbols = "IVXLCDM"
    power = 3

    sym = ""

    while num > 0:
        multiplier = 10 ** power
        digit = num // multiplier
        num %= multiplier

        if digit == 9:
            sym += symbols[power * 2]
            sym += symbols[power * 2 + 2]
            digit -= 9
        elif digit == 4:
            sym += symbols[power * 2]
            sym += symbols[power * 2 + 1]
            digit -= 4
        elif digit >= 5:
            sym += symbols[power * 2 + 1]
            digit -= 5

        sym += symbols[power * 2] * digit

        power -= 1

    return sym

# Example usage
num = int(input("Enter an integer: "))
roman_numeral = intToRoman(num)
print(f"Roman numeral: {roman_numeral}")
