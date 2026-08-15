import tkinter
import json
class Todoapp:
    def __init__(self, window):
        self.window = window
        self.window.title("Todo-list")
        self.label_task = tkinter.Label(self.window, text="Задание", font=("Arial", 17))
        self.label_task.pack()
        self.entry_task = tkinter.Entry(self.window)
        self.entry_task.pack()
        self.label_time = tkinter.Label(self.window, text="Время", font=("Arial", 17))
        self.label_time.pack(pady=(20, 0))
        self.entry_time = tkinter.Entry(self.window)
        self.entry_time.pack()
        self.add_button1 = tkinter.Button(self.window, text="Добавить задачу", font=("Arial", 10), command=self.add_task)
        self.add_button1.pack(pady=15)
        self.tasks_label = tkinter.Label(self.window, text="Список пуст", font=("Arial", 12), justify="left")
        self.tasks_label.pack(pady=20)
        self.tasks = []
    def add_task(self):
        time = self.entry_time.get()
        task = self.entry_task.get()
        task_data = {"task": task, "time": time, "done": False}
        self.tasks.append(task_data)
        text = ""
        for t in self.tasks:
            text += f"{t['task']} - {t['time']}\n"
        self.tasks_label.config(text=text)
        self.save_tasks()
    def save_tasks(self):
        file = open("todoapp.json", "w")
        json.dump(self.tasks, file, ensure_ascii=False)
        file.close()
window = tkinter.Tk()
app = Todoapp(window)
window.mainloop()

