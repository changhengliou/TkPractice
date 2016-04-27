from tkinter import *

master = Tk()

group = LabelFrame(master, text="Group", padx=5, pady=5, relief=RIDGE)
group.pack(padx=10, pady=10)

w = Entry(group)
w.pack()
s = Entry(group)
s.pack()

mainloop()