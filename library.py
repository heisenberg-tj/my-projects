# Library
import tkinter
import json
file = open("books.json", "r")
saved_data = json.load(file)
file.close()
print(saved_data)
window = tkinter.Tk()
window.title("Библиотека")
class Book:
    def __init__(self, name, author, status="На полке"):
        self.name = name
        self.author = author
        self.status = status
    def take_book(self):
        self.status = "Взята"
    def return_book(self):
        self.status = "На полке"
book1 = Book("Война и мир", "Лев Толстой")
label1 = tkinter.Label(window, text=f"{book1.name} - {book1.author} - {book1.status}")
label1.pack()
def take_book1():
    book1.take_book()
    label1.config(text=f"{book1.name} - {book1.author} - {book1.status}")
    save_books()
take_label1 = tkinter.Button(window, text="Взять", command=take_book1)
take_label1.pack()
def return_book1():
    book1.return_book()
    label1.config(text=f"{book1.name} - {book1.author} - {book1.status}")
    save_books()
return_label1 = tkinter.Button(window, text="Вернуть", command=return_book1)
return_label1.pack(pady=15)
book2 = Book("Ромео и Джульетта", "Уильям Шекспир")
label2 = tkinter.Label(window, text=f"{book2.name} - {book2.author} - {book2.status}")
label2.pack()
def take_book2():
    book2.take_book()
    label2.config(text=f"{book2.name} - {book2.author} - {book2.status}")
    save_books()
take_label2 = tkinter.Button(window, text="Взять", command=take_book2)
take_label2.pack()
def return_book2():
    book2.return_book()
    label2.config(text=f"{book2.name} - {book2.author} - {book2.status}")
    save_books()
return_label2 = tkinter.Button(window, text="Вернуть", command=return_book2)
return_label2.pack(pady=15)
book3 = Book("1984", "Джордж Оруэлл")
label3 = tkinter.Label(window, text=f"{book3.name} - {book3.author} - {book3.status}")
label3.pack()
def take_book3():
    book3.take_book()
    label3.config(text=f"{book3.name} - {book3.author} - {book3.status}")
    save_books()
take_label3 = tkinter.Button(window, text="Взять", command=take_book3)
take_label3.pack()
def return_book3():
    book3.return_book()
    label3.config(text=f"{book3.name} - {book3.author} - {book3.status}")
    save_books()
return_label3 = tkinter.Button(window, text="Вернуть", command=return_book3)
return_label3.pack(pady=15)
books = [book1, book2, book3]
def save_books():
    all_books = []
    for book in books:
        book_data = {"name": book.name, "author": book.author, "status": book.status}
        all_books.append(book_data)
    file = open("books.json", "w")
    json.dump(all_books, file, ensure_ascii=False)
    file.close()
window.mainloop()