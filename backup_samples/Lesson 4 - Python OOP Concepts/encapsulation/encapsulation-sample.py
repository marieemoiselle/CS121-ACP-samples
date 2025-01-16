class BankAccount:
	def __init__(self):
		self.balance = 0.0

	def get_balance(self):
		return self.balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount

if __name__ == "__main__":
	account = BankAccount()

	print("Initial balance:", account.get_balance())

	account.deposit(3000)
	print("After deposit:", account.get_balance())

	account.withdraw(800)
	print("After withdrawal:", account.get_balance())