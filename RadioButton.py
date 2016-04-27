from tkinter import *

root = Tk()
root.geometry("300x300")
var = IntVar()
label = Label(root, text="Hello There", fg="red", padx=20, justify=LEFT)
label.pack()


def opt1():
    label.configure(text="Option 1 is checked")


def opt2():
    label.configure(text="Option 2 is checked")


def judge():
    if var.get() == 1:
        label.configure(text="Option 1 is applied")
    elif var.get() == 2:
        label.configure(text="Option 2 is applied")


labelR = Label(root)
labelR.pack()

radio1 = Radiobutton(labelR, text="Option 1", variable=var, value=1, )
radio1.pack(anchor=W)

radio2 = Radiobutton(labelR, text="Option 2", variable=var, value=2, )
radio2.pack(anchor=W)

button = Button(labelR, text="Apply", command=judge)
button.pack()
root.mainloop()
