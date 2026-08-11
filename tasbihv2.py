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
    global stage
    count += 1
    count_label.config(text=f"Нажатий: {count}")
    if stage == 1:
        if count == 33:
            stage = 2
            count = 0
            stage_label.config(text="Этап: Альхамдуллилях!")
    elif stage == 2:
        if count == 33:
            count = 0
            stage = 3
            stage_label.config(text="Этап: Аллаху Акбар!")
    elif stage == 3:
        if count == 33:
            count = 0
            stage_label.config(text="Машаллах! Вы завершили зикр!")
def reset():
    global count
    global stage
    count = 0
    stage = 1
    count_label.config(text=f"Нажатий: {count}")
    stage_label.config(text="Этап: Субханналлах!")
button = tkinter.Button(window, text="Нажми", command=on_click)
button.pack()
resetbutton = tkinter.Button(window, text="Сброс", command=reset)
resetbutton.pack()
window.mainloop()