from tkinter import Entry, Label, StringVar, Tk

root = Tk()
root.title("Tuto Tkinter")
root.config(bg='silver')

Label(root, text='Enter your name below:').pack()
my_var = StringVar()
Entry(root, textvariable=my_var, width=10).pack()

root.mainloop()