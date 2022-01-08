from tkinter import Label, Tk, Button
import time

# app_window = Tk()
# app_window.title("Digital Clock")
# app_window.geometry("420x150")
# app_window.resizable(1, 1)
#
# text_font = ("Boulder", 68, 'bold')
# background = "#f2e750"
# foreground = "#363529"
# border_width = 25
#
# label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
# label.grid(row=0, column=1)
#
#
# def digital_clock():
#     time_live = time.strftime("%H:%M:%S")
#     label.config(text=time_live)
#     label.after(200, digital_clock)
#
#
# digital_clock()
# app_window.mainloop()


app = Tk()
app.title("Windows App")
app.geometry("420x150")

label = Label(app,
    text="Hello, Tkinter",
    width=25,
    height=5,
    foreground="#2E37AF",
    background="#2EA9AF"
)
label.grid(row=0,column=0)

def check():
    pass



button = Button(app,
    text="Clock app",
    width=20,
    height=4,
    bg="#ADFF9E",
    fg="#2E0C47",
    activebackground="black",
    activeforeground="white",
    highlightcolor='#AD75AF',
    command=check
)


button.grid(row=1,column=0)
button.bind(check)
app.mainloop()
