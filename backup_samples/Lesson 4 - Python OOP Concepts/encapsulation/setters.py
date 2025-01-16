class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age