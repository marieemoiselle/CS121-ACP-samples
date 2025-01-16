'''
# Superclass (Base class)
class Artist:
    def make_art(self):
        print("The artist makes art")

# Subclass (Derived class) inheriting from Animal
class Singer(Artist):
    # Additional members and methods specific to Dog class can be added here

    -----
# Single Inheritance
# Superclass
class Artist:
    # Fields, constructors, and methods of Artist class

#Subclass inheriting from Artist
class Painter(Artist):
    # Additional members and methods specific to Dog class can be added here

---
Multi-level Inheritance

# Superclass
class Artist:
    # Fields, constructors, and methods of Artist class

# Subclass inheriting from Artist
class Writer(Artist):
    # Additional members and methods specific to Writer class can be added here

# Subclass inheriting from Writer
class Novelist(Writer):
    # Additional members and methods specific to Novelist class can be added here
'''