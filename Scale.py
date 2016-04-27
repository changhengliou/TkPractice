from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)

w = Scale(root, from_=0, to=100, resolution=0.1, label="TestScale")
w.pack()

w = Scale(root, from_=0, to=200, orient=HORIZONTAL, sliderlength=20, length=200)
w.pack()

root.mainloop()
