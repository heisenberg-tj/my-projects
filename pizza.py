# Pizzeria
import time
menu = ["Пепперони, Цена: 100", "Маргарита, Цена: 130", "Пицца четыре сыра, Цена: 150"]
balance = 250
cart = []
last_action_time = 0
print(f"Добро пожаловать в нашу пиццерию! Ваш баланс {balance}")
print(f"Ознакомтесь с меню {menu}")
print("Что бы выйти пропишите exit")
while True:
    a = input("Какую пиццу хотите заказать?: ")
    current_time = time.time()
    if current_time - last_action_time < 3:
        print("Не спамьте! Подождите 3 секунды!")
        time.sleep(3)
        continue
    last_action_time = current_time
    if a.lower() == "пепперони":
        if balance >= 100:
            balance = balance - 100
            print(f"Мы добавили в ваш заказ пиццу Пепперони! На вашем счёте {balance}")
            cart.append("Пицца Пепперони.")
        else:
             print("Недостаточно средств!")
    elif a.lower() == "маргарита":
        if balance >= 130:
            print("Мы добавили в ваш заказ пиццу Маргарита! с вашего банковского счёте снялось 130 сомони!")
            balance = balance - 130
            print(f"Ваш баланс {balance}")
            cart.append("Пицца Маргарита.")
        else:
             print("Недостаточно средств!")
    elif a.lower() in ["пицца четыре сыра", "сыр", "четыре"]:
        if balance >= 150:
            balance = balance - 150
            print(f"В ваш заказ добавлен пицца четыре сыра. Ваш баланс {balance}")
            cart.append("Пицца четыре сыра.")
    elif a.lower() == "exit":
         print("Вы вышли!")
         print(f"Ваш заказ: {cart} ваш баланс {balance}")
         break
    else:
        print("Такой пиццы нет в меню!")