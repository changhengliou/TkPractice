from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)

w = Spinbox(root, from_=0, to=10, values=(1, 2, 4, 8), font=("courier", 14))
w.pack(side=BOTTOM)

text = Text(root, width="100", height="100")
text.pack()
text.insert(END, "Hello There=)")
text.configure(state=DISABLED)  # Disable manual editing

root.mainloop()
