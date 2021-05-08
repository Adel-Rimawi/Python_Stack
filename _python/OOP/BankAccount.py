class Bankaccount:
    def __init__(self, intrate, balance=0):
        self.intrate = intrate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def account_info(self):
        print("Name: ")  # will add later
        print(f"Balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance*self.intrate)
        return self


account1 = Bankaccount(0.05)

account2 = Bankaccount(0.07)


# account1.deposit(1000).deposit(1000).deposit(1000).withdraw(2000).account_info().yield_interest().account_info()

account2.deposit(500).deposit(1500).withdraw(800).withdraw(500).withdraw(100).withdraw(100).yield_interest().account_info()
