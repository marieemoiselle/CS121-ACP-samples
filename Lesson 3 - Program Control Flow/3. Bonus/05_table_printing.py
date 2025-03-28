def print_table():
    # Solution 1: Manually declare list elements
    numbers = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
    
    '''
    Solution 2: Using loops for list declaration

    numbers = []
    value = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(value)
            value += 1
        numbers.append(row)

    Solution 3:
    Using list comprehension
    numbers = [[i*5 + j + 1 for j in range(5)] for i in range(5)]

    '''
    
    for row in range(5):
        # printing the top border
        if row == 0:
            print("+---+---+---+---+---+")
        
        separator = "|"
        for column in range(5):
            separator += f" {numbers[row][column]:2}|"
        print(separator)

        # printing the bottom border
        print("+---+---+---+---+---+")

print_table()