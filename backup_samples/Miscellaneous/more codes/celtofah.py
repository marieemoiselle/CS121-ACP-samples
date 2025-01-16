# Importing the necessary module for input
import sys

# Main function
def main():
    # Prompting the user for input
    print("Enter a Celsius value: ", end="")
    
    # Reading the input from the user
    cel = float(input().strip())
    
    # Converting Celsius to Fahrenheit
    fah = (cel * 9/5) + 32
    
    # Displaying the result
    print(f"{cel:.2f} Celsius is {fah:.2f} Fahrenheit")

# Calling the main function
if __name__ == "__main__":
    main()
