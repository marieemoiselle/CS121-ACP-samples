class Person:
    def __init__(self):
        self._name = ""
        
        # This line initializes an instance variable _name 
        # and sets it to an empty string.
        # The underscore _ prefix is a convention indicating that this 
        # variable is intended to be private and should not be 
        # accessed directly outside the class.
        
    @property
    def name(self):
        return self._name