import math

def sphere_calculations(diameter):
    # Calculate the radius
    radius = diameter / 2

    # Calculate surface area and volume
    surface_area = 4 * math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3

    # Print the results with four decimal places
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Volume: {volume:.2f}")

# Input the diameter of the sphere
diameter = float(input("Enter the diameter of the sphere: "))

# Call the function to perform calculations
sphere_calculations(diameter)
