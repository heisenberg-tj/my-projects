# My project
balance = 2500
info = []
class LoginSystem:
    def __init__(self, password, attempts):
        self.password = password
        self.attempts = attempts
    def check_password(self, entered_password):
        if self.password == entered_password:
            print("Пароль верный, добро пожаловать!")
            print("Вся нужная информация")
            user = input("Какую информацию вы хотите добавить:")
            info.append(user)
            print(f"Актульная информация {info}")
            print("Информация добавлена!")
            a = input("Хотите проверить баланс? Да/Нет: ")
            if a.lower() == "да":
                print(f"Ваш баланс {balance}")
            if a.lower() == "нет":
                print("Вы вышли из системы!")
            return True
        else:
            print(f"Неправильный пароль у вас осталось {self.attempts} попытки")
            self.attempts = self.attempts - 1
            if self.attempts <= 0:
                print("Попытки закончились!")
                return False
    
system1 = LoginSystem(2290, 3)
while True:
    try:
        entered = int(input("Введите пароль:"))
        result = system1.check_password(entered)
        if result == True:
            break
        elif result == False:
            break
    except:
        print("Нужно вводить только цифры!")
        continue
    