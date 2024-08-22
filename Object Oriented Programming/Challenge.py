class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        print("Deposit Accepted")

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"


account1 = Account('Yafet', 3500)

print(account1)
print()
print(account1.owner)
print()
print(account1.balance)
print()
account1.deposit(250)
print()
account1.withdraw(500)
print()
account1.withdraw(5000)



