# For muslims
print("Привет это электронные чётки, надо сказать 33 раза Субханаллах, 33 раза Альхамдулиллях и 33 раза Аллаху Акбар!")
counter = 0
stage = 1
while True:
    input("Нажмите Enter: ")
    counter = counter + 1
    if stage == 1:
        print(f"Вы сказали Субханаллах {counter} раза.")
        if counter == 33:
            print("Машаллах! Вы сказали 33 раза Субханаллах, переходим к Субханаллах!")
            counter = 0
            stage = 2
    elif stage == 2:
        print(f"Вы сказали Альхамдулиллях {counter} раза.")
        if counter == 33:
            print("Машаллах! Вы сказали 33 раза Альхамдулиллях, переходим к Аллаху Акбар!")
            counter = 0
            stage = 3
    elif stage == 3:
        print("Аллаху Акбар!")
        if counter == 33:
            print("Машаллах! Вы сказали 33 раза Аллаху Акбар! Хорошего дня вам!")
            break