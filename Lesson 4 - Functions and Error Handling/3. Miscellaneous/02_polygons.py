from abc import ABC, abstractmethod

# Abstract Base Class for Polygon
class Polygon(ABC):
    def __init__(self, sides):
        self.sides = sides

    @abstractmethod
    def area(self):
        pass

    def display_sides(self):
        print(f"This polygon has {self.sides} sides.")

# Subclass 1: Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)  # Triangle has 3 sides
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Rectangle Sub class
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)  # Rectangle has 4 sides
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Pentagon Sub class (regular)
class Pentagon(Polygon):
    def __init__(self, side_length, apothem):
        super().__init__(5)  # Pentagon has 5 sides
        self.side_length = side_length
        self.apothem = apothem

    def area(self):
        perimeter = self.side_length * 5
        return (perimeter * self.apothem) / 2

# Menu for the user to choose a polygon
print("Choose a polygon:")
print("1. Triangle")
print("2. Rectangle")
print("3. Pentagon")

choice = input("Enter the number of your choice: ")

polygon = None

if choice == "1":
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    polygon = Triangle(base, height)

elif choice == "2":
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    polygon = Rectangle(length, width)

elif choice == "3":
    side_length = float(input("Enter side length of the pentagon: "))
    apothem = float(input("Enter apothem of the pentagon: "))
    polygon = Pentagon(side_length, apothem)

else:
    print("Invalid choice.")

# Display results
if polygon:
    polygon.display_sides()
    print(f"Area: {polygon.area()}")