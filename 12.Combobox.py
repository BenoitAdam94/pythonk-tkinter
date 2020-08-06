from tkinter import Label, Spinbox, StringVar, Tk
from tkinter.ttk import Combobox

root = Tk()
root.title("11 Spinbox")
root.config(bg='silver')

Label(root, text='Choisissez un nombre:').pack()
my_box = Combobox(root, values=(2,4,6,8))
my_box.current(2)
my_box.pack()

root.mainloop()