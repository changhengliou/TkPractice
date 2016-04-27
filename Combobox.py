from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x300")
root.title("ttk Test")
root.resizable(0, 0)

cb = Combobox(root, values=(0, 3, 6, 9))
cb.pack()
cb.current(1)

root.mainloop()
