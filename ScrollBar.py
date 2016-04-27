from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
#root.resizable(0, 0)
"""The process of setting scroll bar is :
   1.Set the widget’s yscrollcommand callbacks to the set method of the scrollbar.
   2.Set the scrollbar’s command to the yview method of the widget."""
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=RIGHT, fill=BOTH)

scrollbar.config(command=listbox.yview)

root.mainloop()
