class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bankaccount(intrate=0.02, balance=0)

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.account.withdraw(amount)
        return self
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def account_info(self):
        print("Name: "+str(self.name))  # will add later
        print(f"Balance: $" + str(self.account.balance))
        return self

    def transfare_money(self, another_user, amount):
        self.account.balance -= amount
        another_user.balance += amount

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



    def yield_interest(self):
        self.balance = self.balance + (self.balance*self.intrate)
        return self

account1 = Bankaccount(0.02)
adel = user("Adel", account1)
adel.make_deposit(500).account_info()