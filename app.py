# services
services = ["Кредит", "Депозит", "Карта"]
for index, service in enumerate(services, start=1):
    print("Номер услуги:", index)
    print("Сама услуга:", service)
    print("-" * 20)
while True:
    choice = int(input("Выберите номер услуги:"))
    if choice == 1:
        print("Вы выбрали кредит")
        break
    elif choice == 2:
        print("Вы выбрали Депозит")
        break
    elif choice == 3:
        print("Вы выбрали Карта")
        break
    else:
        print("Ошибка: Такой услуги нет")