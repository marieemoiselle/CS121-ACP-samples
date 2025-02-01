my_set = {5, 10, 15, 20, 25}

print(10 in my_set)  # Output: True
print(7 in my_set)  # Output: False

set1 = {8, 16}
set2 = {8, 16, 24, 32, 40}

print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True
