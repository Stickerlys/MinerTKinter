from tkinter import *
# from ttime import *
from PIL import ImageTk
import re
from tkinter import messagebox as mb
import Mennu
from consoleMiner import gen_game


import time

# class Clock():
#     def __init__(self):
#         self.root =Tk()
#         self.label =Label(text="", font=('Helvetica', 48), fg='red')
#         self.label.pack()
#         self.update_clock()
#         self.root.mainloop()
#
#     def update_clock(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.root.after(1000, self.update_clock)



def find_digits(btn):
    s = str(btn)
    nums = re.findall(r'\d+', s)
    if nums == []:
        res = 1
    else:
        res = nums[0]
    # nums = [int(i) for i in nums]

    return res


def opn(event, button):
    # print(type(event.widget), event.widget)
    # a = event.widget
    # print("a=", a, "a(str)=", str(a))
    print(find_digits(button))
    num = int(find_digits(button)) - 1
    print(arr)
    if str(arr[0][num]) == "1":
        button.configure(text=str(arr[0][num]), fg="blue", font=("Arial", 12, "bold"))
    if str(arr[0][num]) == "2":
        button.configure(text=str(arr[0][num]), fg="green", font=("Arial", 12, "bold"))
    if str(arr[0][num]) == "3":
        button.configure(text=str(arr[0][num]), fg="red", font=("Arial", 12, "bold"))
    if str(arr[0][num]) == "4":
        button.configure(text=str(arr[0][num]), fg="purple", font=("Arial", 12, "bold"))
    if str(arr[0][num]) == "5":
        button.configure(text=str(arr[0][num]), fg="pink", font=("Arial", 12, "bold"))
    else:
        button.configure(text=str(arr[0][num]), font=("Arial", 12, "bold"))
    # if arr[0][num] == 1:
    #     button.configure(bg="blue")
    # if arr[0][num] == 2:
    #     button.configure(bg="green")
    # if arr[0][num] == 3:
    #     button.configure(bg="red")
    # if arr[0][num] == 4:
    #     button.configure(bg="purple")
    # if arr[0][num] == -1:
    #     button.configure(bg="black")  # какие-то траблы в соотношении массива чисел и массива кнопок

    # print("bef=", buttons[num].cget("state"))
    # buttons[num].config(state="disabled")
    # print("aftr=", buttons[num].cget("state"))

    # image = ImageTk.PhotoImage(file="pctr/FLAG.png")
    # button.configure(image=image)
    # mb.showinfo(message="d")
    # button.configure(bg="red")


def gen_arr(arr):
    print("gen_game: исходный массив:")
    for idx in range(size + 1):
        print(arr[idx])
    print(" ")
    res = []
    for idx in range(1, size + 1):
        for idx2 in range(1, size + 1):
            res.append(arr[idx][idx2])
    return [res]


def onRightClick(event, button):
    # print('Got right mouse button click:',showPosEvent(event))
    if button.cget("bg") == "white":
        button.configure(bg="#cfb6b6")
    else:
        button.configure(bg="white")


buttons = []
size = 8
arr = gen_arr(gen_game(size, 10))


# def update_clock(self):
#     now = time.strftime("%H:%M:%S")
#     self.label.configure(text=now)
#     self.root.after(1000, self.update_clock)

def GameField():
    # tm = Tk()
    gf = Tk()  # нужно как-то замутить родителя
    gf.geometry("700x500")
    gf.title("Бобёр")
    gf.focus_force()
    tm = Label(gf, text="0:00", font=('Helvetica', 25), fg='red')
    global size
    num_bomb = 10
    #size = 16  # int(Mennu.get_mode_value())

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            but = Button(gf, bg="white",  width=4, height=2, text="  ", font=("Arial", 12, "bold"), borderwidth=1,
                         highlightcolor="#aba2a2", activebackground="#aba2a2")

            but.bind("<Button-1>", lambda event, but=but: opn(event, but))
            but.bind("<Button-3>", lambda event, but=but: onRightClick(event, but))  # установить флаг
            buttons.append(but)
            # but.pack(expand=X)
            but.grid(padx=1, pady=1, row=i, column=j)  # row=i, column=j)
    # lb = Label(text="1-blue,\n2-green,\n3-red,\n4-purple")
    # lb.grid(row=size+1, column=size+1)
    tm.grid(row=1, column=size+1)
    gf.mainloop()
