'''
match subject:
    case pattern1:
        Code block if matches
    case pattern2:
        Code blokc if matches
    case _:
        Default case (wildcard)
        if no other pattern matches
'''

num = int(input("Enter a number: "))

match num:
    case 0:
        print("Do you remember the 21st night of September?")
    case 1:
        print("Love was changin' the mind of pretenders")
    case 2:
        print("While chasin' the clouds away.")
    case 3:
        print("Our hearts were ringin' in the key that our souls were singin'")
    case 4:
        print("As we danced in the night, remember")
    case _:
        print("How the stars stole the night away, oh yeah.")

