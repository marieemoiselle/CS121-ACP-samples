from capybara import Capybara

def test_capybara_class():
    # Creating instances of the Capybara class
    capybara1 = Capybara("Biscoff", "M", 5)
    capybara2 = Capybara("Mochi", "M", 3)
    capybara3 = Capybara("Cinnamon", "F", 4)

    # Prompting user to input the test case number
    test_case = int(input("Enter the test case number: "))

    # Displaying attributes of the selected capybara
    if test_case == 1:
        print(f"Test Case 1: Name: {capybara1.name}, Gender: {capybara1.color}, Age: {capybara1.age} years old")
    elif test_case == 2:
        print(f"Test Case 2: Name: {capybara2.name}, Gender: {capybara2.color}, Age: {capybara2.age} years old")
    elif test_case == 3:
        print(f"Test Case 3: Name: {capybara3.name}, Gender: {capybara3.color}, Age: {capybara3.age} years old")
    else:
        print("Invalid test case number")

if __name__ == "__main__":
    test_capybara_class()