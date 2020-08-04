from tkinter import Label, Tk

root = Tk()
root.title("Another Text")

my_label = Label(root, text='Hello world')
my_label.pack()
my_label.config(text='I want another text')

root.mainloop()