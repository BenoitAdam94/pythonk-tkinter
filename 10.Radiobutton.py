from tkinter import Label, Radiobutton, StringVar, Tk

root = Tk()
root.title("08 Checkbutton")
root.config(bg='silver')

Label(root, text='Choisissez une couleur').pack()
my_var = StringVar()
Radiobutton(root, text='jaune', variable=my_var, value='yellow').pack()
Radiobutton(root, text='red', variable=my_var, value='red').pack()
Radiobutton(root, text='blue', variable=my_var, value='blue').pack()


# my_var.get()

root.mainloop()