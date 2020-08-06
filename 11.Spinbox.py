from tkinter import Label, Spinbox, StringVar, Tk

root = Tk()
root.title("11 Spinbox")
root.config(bg='silver')

Label(root, text='Choisissez une couleur:').pack()
my_box = Spinbox(root, from_=4, to=8).pack()

root.mainloop()