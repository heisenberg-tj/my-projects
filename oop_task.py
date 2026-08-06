# OOP task
import json
class Task:
    def __init__(self, task):
        self.task = task
        self.done = False
    def mark_done(self):
        self.done = True
task1 = Task("Покормить питомца.")
task2 = Task("Полить цветы.")
task3 = Task("Помыть посуду.")
tasks = [task1, task2]
tasks.append(task3)
def save_all():
    all_data = []
    for title in tasks:
        title_data = {"task": title.task, "done": title.done}
        all_data.append(title_data)
    file = open("tasks.json", "w")
    json.dump(all_data, file, ensure_ascii=False)
    file.close()
while True:
    for title in tasks:
        if title.done == True:
            continue
        print(title.task)
        a = input(f"Задание:{title.task}: ")
        if a.lower() == "да":
            print(f"Задание {title.task} выполнено!")
            title.mark_done()
            save_all()
        else:
            print("Вы вышли из системы.")
            exit()
