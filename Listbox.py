from tkinter import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)


def apply():
    index = addlist.curselection()  # Method, return index of selection
    for i in index:
        print(i, addlist.get(i))
    label.configure(text="Success Applied")


def toleft():
    index = addlist.curselection()
    for i in index:
        optionlist.insert(END, addlist.get(i))
    for i in index:
        addlist.delete(i)


def toRight():
    index = optionlist.curselection()
    for i in index:
        addlist.insert(END, optionlist.get(i))
        print(i, optionlist.get(i))
    for i in index:
        optionlist.delete(i)


label = Label(text="     Hello     ", font="courier", fg="red", pady=5)
label.grid(row=0, column=1)
# have bug when choose multiple options and one of it is the last one
scrollbar = Scrollbar(root, orient=VERTICAL)
optionlist = Listbox(root, selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
optionlist.grid(row=4, column=0, rowspan=4, padx=30, pady=5)
scrollbar.config(command=optionlist.yview)  # Complex scrollbar with grid layout, still have not solved

addlist = Listbox(root)
addlist.grid(row=4, column=2, rowspan=4, padx=30, pady=5)

buttonleft = Button(root, text=" << ", command=toleft)
buttonleft.grid(row=4, column=1, pady=40)

buttonright = Button(root, text=" >> ", command=toRight)
buttonright.grid(row=5, column=1)

buttonapply = Button(root, text="Apply", command=apply)
buttonapply.grid(row=8, column=0, columnspan=3)

for name in ("John", "Tracy", "Kobe", "Mike", "Nicole", "Youth", "Zigbee"
             , "Anne", "Sara", "Jessica", "Kiv"):
    optionlist.insert(END, name)

root.mainloop()
