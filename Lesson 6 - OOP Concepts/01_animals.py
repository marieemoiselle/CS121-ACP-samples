from abc import ABC, abstractmethod

# Abstraction
class Animal(ABC):
    def __init__(self, name):
        self.__name = name  # Encapsulation

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass

# Inheritance and Polymorphism
class Dog(Animal):
    def make_sound(self):
        return f"{self.get_name()} says: Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.get_name()} says: Meow!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.get_name()} says: Moo!"

# Main program
def main():
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Cow("Daisy")
    ]

    for animal in animals:
        # Polymorphism in action
        print(animal.make_sound())

if __name__ == "__main__":
    main()
