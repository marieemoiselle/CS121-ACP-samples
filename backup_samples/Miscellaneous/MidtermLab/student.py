class Student:
    def __init__(self):
        self._studentID = 0
        self._name = ""
        self._age = 0

    def set_studentID(self, studentID):
        self._studentID = studentID

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_studentID(self):
        return self._studentID

    def get_age(self, studentName):
        if self._name == studentName:
            return str(self._age)
        else:
            return "Forbidden"