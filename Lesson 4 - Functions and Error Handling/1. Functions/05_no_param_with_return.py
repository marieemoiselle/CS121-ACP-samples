import random

def generaterandomnum():
    rnumber = random.randint(0, 99)  
    # Generate a random number between 0 and 99
    return rnumber

def main():
    rndnum = generaterandomnum()  
    # Calling the function

    print("The random number is:", rndnum)

main()

#Output:
#The random number is: 7
