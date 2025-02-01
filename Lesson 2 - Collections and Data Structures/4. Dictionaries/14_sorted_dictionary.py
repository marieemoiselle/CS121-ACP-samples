person = {"name": "Marie", "age": "28", "occupation": "Instructor", "city": "New York"}

# Sorting the dictionary by keys and creating a new sorted dictionary
sorted_person = dict(sorted(person.items()))
print(sorted_person)

# {'age': '28', 'city': 'New York', 'name': 'Marie', 'occupation': 'Instructor'}

# Sorting the dictionary by keys and creating a new sorted dictionary
sorted_person = dict(sorted(person.items()))

# Sorting the dictionary by values and creating a new sorted dictionary
sorted_person_by_age = dict(sorted(person.items(), key=lambda x: x[1]))
