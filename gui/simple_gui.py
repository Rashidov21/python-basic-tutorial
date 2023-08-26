import random
from  tkinter import Tk, Button ,Label

root = Tk() # oddiy oyna obyekt namunasi
root.geometry("400x150") # oynani hajmini belgilash
root.title("Tkinter Python Window") # oyna sarlavhasi


def get_two_random_names():
    with open("./gui/names.txt", "r", encoding="utf-8") as file:
        names = [name for name in file.read().split(",")]
        left = names[len(names) // 2:]
        right = names[:len(names)-1]
        return left[random.randint(0,len(names) // 2)] + right[random.randint(len(names) // 2,len(names))]

lbl = Label(text='0',foreground="black" ,font="Arial", padx=15,pady=10)

def simple_btn_click():
    lbl.config(text=get_two_random_names())

btn = Button(text="Click me !", bg="gray", fg="white", command=simple_btn_click)

lbl.pack()
btn.pack()


root.mainloop() # oynani doimiy ishga tushirish
# print(dir(root))