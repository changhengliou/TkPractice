from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ListTest")
root.geometry("630x320+300+300")
root.resizable(0, 0)

progress = 0
callback = None


def start():
    global progress, callback
    label.configure(foreground="red", text="Progressing")
    progress += 1
    pb.step(1)
    progress_printer.configure(text=str(progress)+"%")
    print("local progress = ", progress)
    callback = root.after(100, start)
    if progress >= 100:
        progress = 0
        root.after_cancel(callback)
        label.configure(foreground="blue", text="Done!")


def stop():
    global progress, callback
    label.configure(foreground="purple", text="Stop progressing")
    root.after_cancel(callback)
    # pb.step(-progress)


pb = Progressbar(root, maximum=100, length=300, mode="determinate")  # determinate & indeterminate
pb.pack(side=TOP, pady=50)

progress_printer = Label(root, text="0%", font=("courier", 16))
progress_printer.pack(pady=10)

label = Label(root, text="Waiting for Progress", font=("courier", 16))
label.pack(side=TOP)

button1 = Button(root, text="Start", command=start)
button1.pack(side=LEFT, padx=100)

button2 = Button(root, text="Stop", command=stop)
button2.pack(side=RIGHT, padx=100)

root.mainloop()
