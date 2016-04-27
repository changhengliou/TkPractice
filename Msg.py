from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)
"""Message can display multiLine Text"""
w = Message(root, text="this is a relatively long message", font=("courier", 16), width=150).pack()

mainloop()
