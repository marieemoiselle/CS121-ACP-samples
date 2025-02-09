numbers = [1, 2, 3, 4, 5]
search_number = 3
index = -1

for i in range(len(numbers)):
    if numbers[i] == search_number:
        index = i
        break

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")