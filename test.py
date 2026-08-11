import tkinter
count = 0
stage = 1
window = tkinter.Tk()
window.title("Электронные чётки")
stage_label = tkinter.Label(window, text="Этап: Субханаллах!")
stage_label.pack()
count_label = tkinter.Label(window, text=f"Нажатий: {count}")
count_label.pack()
def on_click():
    global count
    count += 1
    count_label.config(text=f"Нажатий: {count}")
button = tkinter.Button(window, text="Нажми", command=on_click)
button.pack()
window.mainloop()