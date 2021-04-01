from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
import GameField

darkMode = 0  # булечка для смены тёмной и светлой темы
mode = 1  # 1 - новичок(8х8), 2 - любитель(16х16), 3 - проффесионал(32х32)


def get_mode_value():
    return mode


def create_new_game(event):

    GameField.GameField()


def abt(event):
    mb.showinfo("О разработчиkе", "PO-4\nDeveloped by Kudelya A."
                                  "\nTested by Shiba A.")


def close(event):
    exit()


def menu():
    wd = 13  # ширина кнопок
    root = Tk()
    root.geometry("500x500")
    root.title("Бобёр")

    title = Label(root, text="Бобёр", font=("Arial Bold", 30))
    title.pack(expand=Y)

    start = Button(root, width=wd, text="Начать")
    start.bind("<Button-1>", create_new_game)
    start.pack(expand=Y)

    combo = Combobox(root)
    combo['values'] = (1, 2, 3)
    combo.current(0)  # установите вариант по умолчанию
    combo.pack(expand=1, anchor=SW)  # combo.get() - для получения значения

    settings = Button(root, width=wd, text="Настройки")
    settings.pack(expand=Y)

    about = Button(root, width=wd, text="О разработчике")
    about.bind("<Button-1>", abt)
    about.pack(expand=Y)

    ext = Button(root, width=wd, text="Выход")
    ext.bind("<Button-1>", close)
    ext.pack(expand=Y)

    root.mainloop()

