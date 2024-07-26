# Example of counting occurrences of elements in a list using a dictionary
fruits = ["apple", "banana", "orange", "apple", "grape", "banana"]
fruit_count = {}

for fruit in fruits:
	fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
print(fruit_count)
# Output: {'apple': 2, 'banana': 2, 'orange': 1, 'grape': 1}