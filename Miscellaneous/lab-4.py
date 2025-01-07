def main():
    year = int(input("Enter a year: "))
    
    if (year % 400 == 0):
        print("Leap Year")

    elif (year % 100 == 0):
        print("Not a Leap Year")

    elif (year % 4 == 0):
        print(f"{year} is a eap Year")

    else:
        print(f"{year} is not a Leap Year")
    
if __name__ == "__main__":
    main()