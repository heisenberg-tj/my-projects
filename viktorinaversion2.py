# viktorina version 2
import random
questions = ["Столица России?",
             "Сколько углов у квадрата?",
             "Сколько мусульманину нужно молиться в день?",
             "Сколько сур в Коране?"]
answers = [
    ["москва"],
    ["4", "четыре"],
    ["5", "пять"],
    ["114"]
]
print("Добро пожаловать в игру, надо ответить на несколько вопросов.")
while True:
    if len(questions) == 0:
        print("Вопросы закончились!")
        break
    chosen_question = random.choice(questions)
    print(chosen_question)
    user_answer = input("Ответ: ").strip().lower()
    if chosen_question == "Столица России?" and user_answer.lower().strip() == "москва":
        print("Правильно!")
    elif chosen_question == "Сколько углов у квадрата?" and user_answer.lower().strip() == "4" or user_answer.lower().strip() == "четыре":
        print("Правильно!")
    elif chosen_question == "Сколько мусульманину нужно молиться в день?" and user_answer.lower().strip() == "5" or user_answer.lower().strip() == "пять":
        print("Правильно!")
    elif chosen_question == "Сколько сур в Коране?" and user_answer.lower().strip() == "114":
        print("Правильно!")
    else:
        print("Неправильно!")
        break
    questions.remove(chosen_question)

