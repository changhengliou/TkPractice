from tkinter import *


def hello():
    print("hello!")


root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)

counter = 0


def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label=str(counter))

var = IntVar()
var2 = IntVar()

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_checkbutton(label="JPEG", onvalue=1, offvalue=0, variable=var)
filemenu.add_checkbutton(label="PNG", onvalue=1, offvalue=0, variable=var2)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

menu = Menu(menubar, tearoff=0, postcommand=update)  # Postcommand allow changed after click
menu.add_command(label=str(counter))
menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Test", menu=menu)

root.config(menu=menubar)

root.mainloop()
