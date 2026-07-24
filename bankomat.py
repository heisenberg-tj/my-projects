# bank
file = open("balance.txt", "r")
content = file.read()
balance = int(content)
file.close()
while True:
    choice = input("1-баланс, 2-пополнить, 3-снять, 4-выйти: ")
    if choice == "1":
        print(f"Ваш баланс: {balance}")
    elif choice == "2":
        amount = int(input("Введите сумму которую хотите пополнить:"))
        balance = balance + amount
        print(f"Вы пополнили сумму вашего банковского счёта, теперь на вашем счёте: {balance}")
    elif choice == "3":
        snyat = int(input("Введите сумму которую хотите снять: "))
        if snyat > balance:
            print("Недостаточно средств!")
        else:
            balance = balance - snyat
            print(f"Вы сняли с вашего банковского счёта {snyat}, на вашем счету теперь {balance}")
    elif choice == "4":
        file = open("balance.txt", "w")
        file.write(str(balance))
        file.close()
        print("Вы вышли с системы!")
        break