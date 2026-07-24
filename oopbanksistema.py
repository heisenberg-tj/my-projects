class Bankomat:
    def __init__(self, balance):
        self.balance = balance
    def add_money(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            print(f"Вы сняли {amount}")
            self.balance = self.balance - amount
account1 = Bankomat(1000)
account1.add_money(500)
account1.withdraw(300)
print(account1.balance)
