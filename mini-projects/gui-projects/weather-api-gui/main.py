from tkinter import Tk, Button, Label,Entry
from config import getWeather
win = Tk()
win.title("Weather App")
win.geometry("300x180")

def input_window():
    w = Tk()
    w.title("Enter your city name ")
    w.geometry("400x180")
    i = Entry(w,)
    i.pack()
    i.mainloop()
    return True

button = Button(win,
    text="Weather",
    width=10,
    height=5,
    bg="#ADFF9E",
    fg="#2E0C47",
    command=input_window
)
label = Label(win,
              text="Weather",
              width=10,
              height=5,
              bg="#ADFF9E",
              fg="#2E0C47",
              )
button.pack()
win.mainloop()