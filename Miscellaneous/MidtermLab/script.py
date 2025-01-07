from student import Student
from tester import Tester

def main():
    student = Student()

    student.set_studentID(int(input("Enter student ID: ")))
    student.set_name(input("Enter name: "))
    student.set_age(int(input("Enter age: ")))

    Tester.test(student)


if __name__ == "__main__":
    main()