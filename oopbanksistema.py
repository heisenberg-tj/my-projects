import json
class Bankomat:
    def __init__(self, filename):
        self.filename = filename
        file = open(self.filename, "r")
        data = json.load(file)
        self.balance = data["balance"]
        file.close()
    def add_money(self, amount):
        self.balance = self.balance + amount
        print(f"Вы пополнили сумму вашего банковского счёта теперь на нём {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            print(f"Вы сняли {amount} теперь на вашем банковском счёте {self.balance}")
            self.balance = self.balance - amount
    def save(self):
        file = open(self.filename, "w")
        data = {"balance": self.balance}
        json.dump(data, file)
        file.close()
class SavingAccount(Bankomat):
    def add_interest(self):
        self.balance = self.balance + self.balance * 0.05
        print(f"Начислены проценты {self.balance}")
class CreditAccount(Bankomat):
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Вы сняли {amount}, теперь на вашем банковском счёте {self.balance}")
account2 = SavingAccount("account2.json")
account2.add_money(100)
account2.add_interest()
print(account2.balance)
account1 = Bankomat("account1.json")
print(account1.balance)
accounts = [account1, account2]
for acc in accounts:
    print(acc.balance)
    acc.save()
while True:
    choice = input("1=баланс, 2-пополнить, 3-снять, 4-выйти: ")
    if choice == "1":
        print(f"Баланс вашего счёта {account1.balance}:")
    elif choice == "2":
        try:
            amount = int(input("Сумма:"))
            account1.add_money(amount)
        except ValueError:
            print("Это не число!")
    elif choice == "3":
        try:
            summa = int(input("Введте сумму которую хотите снять: "))
            account1.withdraw(summa)
        except ValueError:
            print("Это не число!")
    elif choice == "4":
        account1.save()
        print("Вы вышли из системы")
        break
      