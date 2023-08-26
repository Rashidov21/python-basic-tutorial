import locale
locale.setlocale(locale.LC_ALL, "UZ_uz")
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.geometry("500x100")
root.title('Clock')
root.config(background='gray')


def show_time():
	string = strftime('%H:%M:%S %A')
	lbl.config(text=string)
	lbl.after(1000, show_time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('Poppins', 40, 'bold'),
			background='gray',
			foreground='#232328')
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
show_time()
mainloop()
