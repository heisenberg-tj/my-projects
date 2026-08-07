# Dostavka
file = open("restaurant.balance.txt", "r")
balance = int(file.read())
file.close()
print(f"Здравствуйте добро пожаловать в наш онлайн ресторан! Ваш баланс {balance}")
menu = ["Паста, Цена: 150", "Пицца, Цена: 100", "Бургер, Цена: 50", "Кока-Кола, Цена: 15", "Торт, Цена: 35"]
while True:
    answer = input("Что хотите заказать?(Чтобы вызвать меню напишите menu): ")
    if answer.lower() == "menu":
        print(menu)
    elif answer.lower() == "паста":
        a = input("Подтвержадете оплату?(Да/Нет): ")
        if a.lower() == "да":
            if balance < 150:
                print("Недостаточно средств.")
                continue
            balance = balance - 150
            print(f"Оплата успешно прошла! Ваш баланс {balance}.")
        else:
            print("Вы вышли!")
            break
    elif answer.lower() == "пицца":
        a = input("Подтверджаете оплату?(Да/Нет): ")
        if a.lower() == "да":
            if balance < 100:
                print("Недостаточно средств.")
                continue
            balance = balance - 100
            print(f"Оплата успешно прошла! Ваш баланс {balance}.")
    elif answer.lower() == "бургер":
        a = input("Подтверждаете оплату?(Да/Нет): ")
        if a.lower() == "да":
            if balance < 50:
                print("Недостаточно средств.")
                continue
            balance = balance - 50
            print(f"Оплата успешно прошла! Ваш баланс {balance}.")
    elif answer.lower() == "кока-кола" or answer.lower() == "кола" or answer.lower() == "кока":
        a = input("Подтверждаете оплату?(Да/Нет): ")
        if a.lower() == "да":
            if balance < 15:
                print("Недостаточно средств.")
                continue
            balance = balance - 15
            print(f"Оплата успешно прошла! Ваш баланс {balance}.")
    elif answer.lower() == "торт":
        a = input("Подтверждаете оплату?(Да/Нет): ")
        if a.lower() == "да":
            if balance < 35:
                print("Недостаточно средств.")
                continue
            balance = balance - 35
            print(f"Оплата прошла успешно, ваша баланс {balance}")
        else:
            break
    file = open("restaurant.balance.txt", "w")
    file.write(str(balance))
    file.close()