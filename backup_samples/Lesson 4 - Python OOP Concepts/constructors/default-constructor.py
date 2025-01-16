class Person:
    def __init__ (self, name = "Jocson Magnaye", age = 0):
        self.name = name
        self.age = age

person = Person()
print(person.name)
print(person.age)

print("---------------------------------------")

person2 = Person("James Vladimir", 21)
print(person2.name)
print(person2.age)
