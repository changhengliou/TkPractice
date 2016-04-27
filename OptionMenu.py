from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)


def ok():
    print("value is", var.get())
    msg.configure(text="Value " + str(var.get()) + " is checked!")
    root.after(3000, aft)


def aft():
    msg.configure(text="HELLO")


var = StringVar(root)
var.set("one")  # default value

msg = Message(root, text="HELLO", width=400, font=("courier", 16), fg="red")
msg.pack()

w = OptionMenu(root, var, "one", "two", "three")
w.pack(pady=20)

button = Button(root, text="Apply", command=ok).pack()

root.mainloop()
