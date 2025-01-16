def calculate_hearts(name1, name2):
    # define the HEARTS letters and their meanings
    HEARTS = "HEARTS"
    meanings = {
        "H": "Happiness",
        "E": "Euphoria",
        "A": "Admiration",
        "R": "Romance",
        "T": "Trust",
        "S": "Support"
    }

    # convert names to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # find the unique letters in each name
    unique_name1 = ''.join([char for char in name1 if char not in name2])
    unique_name2 = ''.join([char for char in name2 if char not in name1])

    # get the total unique leftover letters
    total_unique_letters = len(unique_name1) + len(unique_name2)

    # find the result by wrapping around the HEARTS string
    result_index = (total_unique_letters - 1) % len(HEARTS)
    result_letter = HEARTS[result_index]
    result_meaning = meanings[result_letter]

    # returns the result
    return total_unique_letters, result_letter, result_meaning


# get name values
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

# solve and display the result
total, letter, meaning = calculate_hearts(name1, name2)
print(f"Result: {total} so {meaning}")