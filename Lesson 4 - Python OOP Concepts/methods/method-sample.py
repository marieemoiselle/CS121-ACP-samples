class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def display_info(self):
		print(f"Name: {self.name}, Age: {self.age}")

# Create instances of Person class
person1 = Person("Fatima Marie", 27)
person2 = Person("Gerald James", 26)
person3 = Person("Jerome", 29)

# Call the display_info method for each person
person1.display_info()
person2.display_info()
person3.display_info()