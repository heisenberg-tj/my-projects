# cars
class Car: # шаблон машины
    def __init__(self, brand, color): # запускаеться при создании новой машины
        self.brand = brand # сохраняем марку в конкретный объект
        self.color = color
    def drive(self):
        print(self.brand + " едет") # действие машины    
car1 = Car("Toyota", "Белый")
car1.drive()
print(car1.brand)
print(car1.color)
print(car1.drive)
car2 = Car("BMW", "Чёрный")
car2.drive()
print(car2.brand)
print(car2.color)
print(car2.drive)
class Person: # человек как и машина сверху
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Привет меня зовут {self.name} мне {self.age}")    
human1 = Person("Александр", "29")
human2 = Person("Джон", "25")
print(human1.name)
print(human1.age)
print(human2.name)
print(human2.age)
human1.greet()
human2.greet()