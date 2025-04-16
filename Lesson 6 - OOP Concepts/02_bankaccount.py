from abc import ABC, abstractmethod

# Abstraction
class BankAccount(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.__account_number = account_number  # Encapsulation
        self.__owner = owner
        self.__balance = balance
        self.__transaction_history = []

    def get_account_number(self):
        return self.__account_number

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited ₱ {amount:,.2f}")
            print(f"Deposited ₱ {amount:,.2f}. New balance: ₱ {self.__balance:,.2f}")
        else:
            print("Invalid deposit amount.")

    def _update_balance(self, amount, description=""):
        self.__balance += amount
        if description:
            self.__transaction_history.append(description)

    def show_transaction_history(self):
        print("\nTransaction History:")
        if not self.__transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.__transaction_history:
                print("-", transaction)

    @abstractmethod
    def withdraw(self, amount):
        pass

# Inheritance and Polymorphism
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._update_balance(-amount, f"Withdrew ₱ {amount:,.2f} from Savings")
            print(f"Withdrew ₱ {amount:,.2f} from Savings. New balance: ₱ {self.get_balance():,.2f}")
        else:
            print("Insufficient funds in Savings Account.")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=1000):
        super().__init__(account_number, owner, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.__overdraft_limit:
            self._update_balance(-amount, f"Withdrew ₱ {amount:,.2f} from Checking")
            print(f"Withdrew ₱ {amount:,.2f} from Checking. New balance: ₱ {self.get_balance():,.2f}")
        else:
            print("Overdraft limit exceeded.")

# Main Program with User Input
def main():
    print("🐷 Welcome to Piggy Bank!💰\n")
    print("Choose your Account Type:")
    print("1 - 💸 Savings Account")
    print("2 - 💹 Checking Account")
    
    choice = input("Enter your choice: ")
    name = input("Enter account holder's name: ")
    acc_num = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))

    if choice == "1":
        account = SavingsAccount(acc_num, name, balance)
    elif choice == "2":
        account = CheckingAccount(acc_num, name, balance)
    else:
        print("Invalid account type selected.")
        return

    while True:
        print("\n🏦 Menu:")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - Show Balance")
        print("4 - Transaction History")
        print("5 - Exit")

        option = input("Choose an option: ")

        if option == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif option == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif option == "3":
            print(f"Current Balance: ₱ {account.get_balance():,.2f}")
        elif option == "4":
            account.show_transaction_history()
        elif option == "5":
            print("Thank you for using Piggy Bank! 🐽💕")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()