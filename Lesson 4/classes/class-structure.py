'''
class ClassName:
    # Fields (attributes) - define the state of the object
    def __init__(self, parameter1, parameter2, ...):
        # constructor code
        self.fieldName1 = parameter1
        self.fieldName2 = parameter2
        # ...

# Methods - define the behavior of the object
    def methodName1(self, parameter1, parameter2, ...):
        # method code
        pass

    def methodName2(self, parameter1, parameter2, ...):
        # method code
        pass
# ...
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_bonjour(self):
        print(f"Bonjour, my name is {self.name}, {self.age} years old.")

    def add_age(self):
        self.age += 1
        print(f"I am turning {self.age} years old.")

person = Person("Fatima Marie", age = 27)
# Person p = new Person ("Fatima Marie", 27);
person.say_bonjour()
person.add_age()