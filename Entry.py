from tkinter import *


def gettext():
    label.configure(text=entry.get())
    entry.delete(0, len(entry.get()))


root = Tk()
root.geometry("300x300")

label = Label(root, text="", fg="red", font="courier", )
label.pack()

entry = Entry(root, bd=3, justify=CENTER, selectbackground="#f38769", show="$")
entry.pack()

button = Button(root, text="Enter", command=gettext).pack()
root.mainloop()
