import random
question = ["Столица Таджикистана?:", "2+2=", "5x2=", "Сколько в мире стран?(цифрами):", "Сборная какой страны выйграла ЧМ 2026?:", "Сколько углов в квадрате?:"]
while True:
    if len(question) == 0:
        print("Вопросы закончились!")
        break
    chosen_question = random.choice(question)
    print(chosen_question)
    answer = input("Ответ:")
    if chosen_question == "Столица Таджикистана?:" and answer.lower() == "душанбе":
        print("Правильно!")
    elif chosen_question == "2+2=" and (answer.lower() == "4" or answer.lower() == "четыре"):
        print("Правильно!")
    elif chosen_question == "5x2=" and (answer.lower() == "10" or answer.lower() == "десять"):
        print("Правильно!")
    elif chosen_question == "Сколько в мире стран?(цифрами):" and answer.lower() == "195":
        print("Правильно!")
    elif chosen_question == "Сборная какой страны выйграла ЧМ 2026?:" and answer.lower() == "испания":
        print("Правильно!")
    elif chosen_question == "Сколько углов в квадрате?:" and (answer.lower() == "4" or answer.lower() == "четыре" or answer.lower() == "four"):
        print("Правильно!")
    else:
        print("Неправильно!")
        break
    question.remove(chosen_question)