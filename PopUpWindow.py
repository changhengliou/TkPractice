from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("280x200+300+300")
root.resizable(0, 0)


def pop():
    top = Toplevel()
    top.title("About this application...")

    msg = Message(top, text="Surprise!", width=300, font=("courier", 16))
    msg.pack(expand=TRUE)

    button = Button(top, text="OK", command=top.destroy)
    button.pack()


button = Button(root, text="Surprise Here=)", font=("courier", 12), command=pop)
button.pack(pady=75)

root.mainloop()
