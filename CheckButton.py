from tkinter import *

root = Tk()
var = IntVar()
var2 = IntVar()


def com():
    if var.get() == 1:
        label.configure(fg="red")
    if var2.get() == 1:
        label.configure(text="Hello! 12345678")


check1 = Checkbutton(root, text="Red", variable=var, onvalue=1, offvalue=0, command=com, indicatoron=False).pack()
check2 = Checkbutton(root, text="Hello", variable=var2, onvalue=1, offvalue=0, command=com).pack()
label = Label(root, text="12345678")
label.pack()

root.mainloop()
