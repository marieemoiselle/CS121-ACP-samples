from cat import Cat
#import the Cat class from the cat module

def test_cat_class():
    cat1 = Cat("Matcha", "Gray", 5)

    #display attributes of cat1
    print(f"Name: {cat1.name}, Age: {cat1.age}, Color: {cat1.color}")

test_cat_class()