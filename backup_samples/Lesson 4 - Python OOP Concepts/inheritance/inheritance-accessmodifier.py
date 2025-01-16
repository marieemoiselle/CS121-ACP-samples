'''
# Superclass
class Artist:
    def __init__(self, medium):
        self._medium = medium

# Method with protected access modifier
    def _some_protected_method(self):
        # Method implementation

# Method with private access modifier
    def __some_private_method(self):
        # Method implementation

# Subclass inheriting from Artist
class Painter(Artist):
    def __init__(self, medium):
        super().__init__(medium)
        # Accessing the protected field and method from the base class
        medium = self._medium
        self._some_protected_method()

    # Private method is not accessible here
'''