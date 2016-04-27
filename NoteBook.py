from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x300")
root.title("ttk Test")
root.resizable(0, 0)

nb = Notebook(root, width=400, height=400)

tab1 = Frame(nb)
tab2 = Frame(nb)
tab3 = Frame(nb)

nb.add(tab1, text="Tab1")
nb.add(tab2, text="Tab2")
nb.add(tab3, text="Tab3")

label = Label(tab1, text="Hello")
label.pack()

sep = Separator(tab1, orient="horizontal")
sep.pack(fill=BOTH)

nb.pack()

root.mainloop()
