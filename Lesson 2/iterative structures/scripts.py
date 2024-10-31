try:
    value = int(input("Enter an upper bound: "))
    if value < 0:
        raise ValueError("Please enter a non-negative integer.")
    
    for i in range(value):
        print(f"[{i}] Join us in SCRIPT! ♡")
        
except ValueError as e:
    print(f"Invalid input: {e}")
