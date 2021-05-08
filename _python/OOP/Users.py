class user:
    def __init__(self, name, balance=0):
        self.balance = balance
        self.name = name

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount

    def display_user_balance(self):
        print("User name is "+self.name)
        print("The balance is: $"+str(self.balance))

    def transfare_money(self, another_user, amount):
        self.balance -= amount
        another_user.balance += amount


adel = user("adel", 2000)
murad = user("murad", 1500)
alaa = user("alaa", 2500)


# adel.make_deposit(100)
# adel.make_deposit(500)
# adel.make_deposit(150)
# adel.make_withdrawal(300)
# adel.display_user_balance()

# adel.transfare_money(murad, 500)
# print(adel.balance)
# print(murad.balance)


# murad.make_deposit(100)
# murad.make_deposit(300)
# murad.make_withdrawal(50)
# murad.make_withdrawal(150)
# murad.display_user_balance()


alaa.make_deposit(100)
alaa.make_withdrawal(50)
alaa.make_withdrawal(50)
alaa.make_withdrawal(50)
alaa.display_user_balance()


adel.transfare_money(alaa, 500)
adel.display_user_balance()
alaa.display_user_balance()
