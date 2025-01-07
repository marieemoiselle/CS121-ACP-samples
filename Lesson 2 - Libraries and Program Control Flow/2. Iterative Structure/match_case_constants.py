# match case with constants

def greet_guest(person):
    match person:
        case "A":
            print("Clock strikes upon the hour")
        case "B":
            print("And the sun begins to fade")
        case "C":
            print("Still enough time to figure out")
        case _:
            print("How to chase my blues away")

greet_guest("A")
greet_guest("a")