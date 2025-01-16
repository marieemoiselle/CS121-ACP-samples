# Dictionary with initial key-value pairs
person = {"name": "Marie", "age": 27, "occupation": "Instructor", "city": "New York"}

person.pop("city") # Removes the "city" key and its value
del person["age"] # Removes the "age" key and its value

print(person)
# Output:
# {'name': 'Marie', 'occupation': 'Instructor'}