# test
print("Привет, добро пожаловать в игру!")
ochki = 0
a = input("Что ты ел сегодня?, 1 - Фастфуд, 2 - Домашняя еда: ")
if a == "2":
    ochki = ochki + 10
elif a == "1":
    ochki = ochki - 10
else:
    print("Неверное значение!")
b = input("Сколько ты сегодня программировал? 1 - 0 минут, 2 - 30+ минут: ")
if b == "2":
    ochki = ochki + 10
elif b == "1":
    ochki = ochki - 10
else:
    print("Неверное значение!")
c = input("Занимался ли ты сегодня спортом? 1-Да, 2-Нет: ")
if c == "1":
    ochki = ochki + 10
elif c == "2":
    ochki = ochki - 10
else:
    print("Неверно значение!")
print(f"Очки: {ochki}")
if ochki < 10:
    print("Тебе нужно больше двигаться и есть полезную еду!!")
elif ochki >= 10:
    print("Молодец, ты сегодня хорошо постарался")
