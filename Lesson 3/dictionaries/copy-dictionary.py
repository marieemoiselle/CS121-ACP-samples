# Dictionary with initial key-value pairs
person1 = {"name": "Marie", "age": 27, "occupation": "Instructor", "city": "New York"}
person2 = {"name": "Gerald", "age" : 26, "occupation": "Instructor", "city": "Paris"}

# Using copy() method
copied_dict = person1.copy()
print(copied_dict)

# Using dict() constructor
dict_copied = dict(person2)
print(dict_copied)

# 
# {'name': 'Marie', 'age': 27, 'occupation': 'Instructor', 'city': 'New York'}
# {'name': 'Gerald', 'age': 26, 'occupation': 'Instructor', 'city': 'Paris'}
