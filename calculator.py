# Calculator
while True:
    print("Привет, это калькулятор!")
    num1 = int(input("Первое число:"))
    operation = input("Выберите значение: [+, -, *, /]: ")
    num2 = int(input("Второе число:"))
    if operation == '+':
        print(f"Результат: {num1 + num2}")
    elif operation == "-":
        print(f"Результат: {num1 - num2}")
    elif operation == "*":
        print(f"Результат: {num1 * num2}")
    elif operation == "/":
        print(f"Результат: {num1 / num2}")
    else:
        print("Неправильное значение!")
        exit()