class Student:
    def __init__(self, name, age, department="Undeclared"):
        self.name = name
        self.age = age
        self.department = department

    # Constructor with partial information (constructor chaining)
    def __init__(self, name, age):
        super().__init__(name, age, "Undeclared")

# Rest of the class members and methods