from tkinter import Button, DISABLED, Entry, Label, StringVar, Tk

root = Tk()
root.title("Tuto Tkinter")
root.config(bg='silver')

Label(root, text='Hello world').pack()

button1 = Button(root, text='Activé', command=lambda: None)
button2 = Button(root, text='Modifier lautre bouton',
                    command=lambda: button1.config(text='desactive',
                    state=DISABLED,
                    cursor='watch'))


button1.pack()
button2.pack()
root.mainloop()