from abc import ABC, abstractmethod
import math

#Interface
class Shape(ABC):
    #Abstract Method
    @abstractmethod #decorator
    def get_area(self):
        pass


# Implementation of Shape interface
# class Rectangle implements Shape
class Rectangle(Shape):
    #Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
# Implementation of Shape interface 
class Circle(Shape):
    #Constructor
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * (self.radius**2)
    
class Triangle(Shape):
    #Constructor
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
       return 0.5 * self.base * self.height
    
rectangle = Rectangle(4.3, 5.334)
circle = Circle(8.5)
triangle = Triangle(6.3, 5.2)

print(f"Area of rectangle: {rectangle.get_area():.2f}.")
print(f"Area of circle: {circle.get_area():.2f}.")
print(f"Area of triangle: {triangle.get_area():.2f}")