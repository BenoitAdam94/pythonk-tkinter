from tkinter import BooleanVar, Checkbutton, Button, DISABLED, Entry, Label, StringVar, Tk

root = Tk()
root.title("08 Checkbutton")
root.config(bg='silver')

Label(root, text='Hello world').pack()
my_var = BooleanVar()
Checkbutton(root, text="Check if you love Python",
            variable=my_var, bg='brown', fg='white').pack()


root.mainloop()