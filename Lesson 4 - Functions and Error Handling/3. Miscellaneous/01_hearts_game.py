def hearts_game(name1, name2):
    # convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # convert names to sets to determine unique leftover letters
    set1 = set(name1)
    set2 = set(name2)

    unique_name1 = set1 - set2
    unique_name2 = set2 - set1

    total_unique_letters = len(unique_name1) + len(unique_name2)

    # HEARTS conversions
    hearts = ["Happiness", "Euphoria", "Admiration", "Romance", "Trust", "Support"]

    # getting the result by counting around HEARTS
    index = (total_unique_letters - 1) % len(hearts)  # wrap around
    return total_unique_letters, hearts[index]

# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get the result number and status
result_number, result_status = hearts_game(name1, name2)

# Print result
print(f"Results: {result_number} - Meaning: {result_status}")