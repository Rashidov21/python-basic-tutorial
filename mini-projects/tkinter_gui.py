from tkinter import *
import random
# 1km = 0.62 ml
# 1ml = 1.62km

def click():
    num = random.randint(1, 6)
    answer["text"] = num
    answer["fg"] = '#333'


window = Tk()
window.title("Roll a dice")
window.geometry("200x200")

button1 = Button(text="Roll", font="Poppins", command=click)
button1["bg"] = "#333"
button1["fg"] = "#fff"
button1.place(x=70, y=10, width=60, height=25)
answer = Message(text="", font=("Poppins", 40))
answer.place(x=70, y=100, width=60, height=60)

window.mainloop()

# import schedule
# import time
# from tkinter import *
# from alarm import alarm


# def set_alarm():
#     hour = textbox1.get()
#     minute = textbox2.get()
#     schedule.every().day.at(f"{hour}:{minute}").do(alarm)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# window = Tk()
# window.geometry("400x200")
# label1 = Label(text="Enter hour: ")
# label2 = Label(text="Enter minute: ")
# label1.place(x=20, y=20)
# label2.place(x=20, y=50)
# textbox1 = Entry(text="")
# textbox1.place(x=120, y=20, width=200, height=25)
# textbox1["justify"] = "left"
# textbox1.focus()
# button1 = Button(text="Set alarm", command=set_alarm)
# button1.place(x=120, y=80, width=120, height=25)
# textbox2 = Entry(text="")
# textbox2.place(x=120, y=50, width=200, height=25)
# textbox2["bg"] = "white"
# textbox2["fg"] = "red"

# window.mainloop()

# # pip install tk
# from tkinter import *


# def call():
#     msg = Label(window, text="You pressed the button")
#     msg.place(x=30, y=50)
#     button["bg"] = "blue"
#     button["fg"] = "white"


# # window = Tk()  # oyna obyekti
# # window.geometry("500x220")  # oynani hajmi
# window = Tk()
# window.title("Alarm Python")
# window.geometry("450x100")
# entry_box = Entry(text=0)
# button = Button(text="Press me", command=call)  # Tugma obyekti
# # tugmani oyna ichida qayerda turishi
# button.place(x=30, y=20, width=120, height=25)

# window.mainloop()  # bu oynani ishga tushirish
