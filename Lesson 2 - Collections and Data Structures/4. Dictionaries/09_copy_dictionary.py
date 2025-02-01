# Dictionary with initial key-value pairs
person1 = {"name": "Marie", "age": 28, "occupation": "Instructor", "city": "New York"}
person2 = {"name": "Jake", "age" : 29, "occupation": "Accountant", "city": "Paris"}

# Using copy() method
copied_dict = person1.copy()
print(copied_dict)

# Using dict() constructor
dict_copied = dict(person2)
print(dict_copied)

# {'name': 'Marie', 'age': 28, 'occupation': 'Instructor', 'city': 'New York'}
# {'name': 'Jake', 'age': 29, 'occupation': 'Instructor', 'city': 'Paris'}