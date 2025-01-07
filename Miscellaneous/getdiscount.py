def calculate_discount(purchase_amount):
    if purchase_amount > 5000:
        discount = 0.10  # 10% discount
    else:
        discount = 0.05  # 5% discount

    discount_amount = purchase_amount * discount
    final_amount = purchase_amount - discount_amount

    print(f"Initial Purchase Amount: {purchase_amount:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"Final Price: {final_amount:.2f}")

# Loop to allow user to try again
while True:
    purchase_amount = float(input("Enter the total purchase amount: "))
    calculate_discount(purchase_amount)
    
    try_again = input("Do you want to try again? (yes/no): ").lower()
    if try_again != 'yes':
        print("Thank you!")
        break
