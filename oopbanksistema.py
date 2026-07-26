class Bankomat:
    def __init__(self):
        file = open("oop_balance.txt", "r")
        content = file.read()
        self.balance = int(content)
        file.close()
    def add_money(self, amount):
        self.balance = self.balance + amount
        print(f"Вы пополнили сумму вашего банковского счёта теперь на нём {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            print(f"Вы сняли {amount}")
            self.balance = self.balance - amount
    def save(self):
        file = open("oop_balance.txt", "w")
        file.write(str(self.balance))
        file.close()
account1 = Bankomat()
print(account1.balance)
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