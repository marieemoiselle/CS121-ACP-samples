class Tester:
    def get_field_value(obj, field_name):
        dict_fields = obj.__dict__
        return dict_fields[field_name]

    def get_method(obj, method_name):
        function = getattr(obj, method_name)
        return function

    def test(student):
        code = int(input("Enter code: "))

        if code == 1:
            name = Tester.get_field_value(student, "_name")
            studentID = Tester.get_field_value(student, "_studentID")
            age = Tester.get_field_value(student, "_age")

            if name is not None and studentID is not None and age is not None:
                print("SUCCESS")
            else:
                print("FAILED")
        elif code == 2:
            getName = Tester.get_method(student, "get_name")
            getStudentID = Tester.get_method(student, "get_studentID")
            getAge = Tester.get_method(student, "get_age")

            if getName is not None and getStudentID is not None and getAge is not None:
                try:
                    print(getName())
                    print(getStudentID())
                    print(getAge(getName()))
                    print("SUCCESS")
                except Exception:
                    print("FAILED")
            else:
                print("FAILED")
        elif code == 3:
            setName = Tester.get_method(student, "set_name")
            getName = Tester.get_method(student, "get_name")

            if setName is not None and getName is not None:
                try:
                    newName = input("Enter new name: ")
                    setName(newName)
                    nameAfter = getName()
                    if nameAfter == newName:
                        print("SUCCESS")
                    else:
                        print("FAILED")
                except Exception:
                    print("FAILED")
            else:
                print("FAILED")
        elif code == 4:
            setAge = Tester.get_method(student, "set_age")
            getAge = Tester.get_method(student, "get_age")

            if setAge is not None and getAge is not None:
                try:
                    newAge = int(input("Enter new age: "))
                    setAge(newAge)
                    ageAfter = getAge(student.get_name())
                    if ageAfter == str(newAge):
                        print("SUCCESS")
                    else:
                        print("FAILED")
                except Exception:
                    print("FAILED")
            else:
                print("FAILED")
        elif code == 5:
            getAge = Tester.get_method(student, "get_age")

            if getAge is not None:
                try:
                    wrongName = input("Enter wrong name: ")
                    result = getAge(wrongName)
                    if result == "Forbidden":
                        print("SUCCESS")
                    else:
                        print("FAILED")
                except Exception:
                    print("FAILED")
            else:
                print("FAILED")
        elif code == 6:
            setStudentID = Tester.get_method(student, "set_studentID")
            getStudentID = Tester.get_method(student, "get_studentID")
            if setStudentID is not None and getStudentID is not None:
                try:
                    newStudentID = int(input("Enter new student ID: "))
                    setStudentID(newStudentID)
                    studentIDAfter = getStudentID()
                    if studentIDAfter == newStudentID:
                        print("SUCCESS")
                    else:
                        print("FAILED")
                except Exception:
                    print("FAILED")
            else:
                print("FAILED")
        else:
            print("Invalid code.")