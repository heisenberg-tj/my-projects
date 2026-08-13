import random
try:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+"
    all_characters = letters + numbers + symbols
    print("----------Генератор супер-паролей----------")
    length = int(input("Введите длинну пароля(например, 12): "))
    password = ""
    for i in range(length):
        random_char = random.choice(all_characters)
        password += random_char
    print("Ваш пароль:", password)
    print("ВНИМАНИЕ! Объязательно сохраните этот пароль куда нибудь!")
except ValueError:
    print("Нужно вводить только цифры!")