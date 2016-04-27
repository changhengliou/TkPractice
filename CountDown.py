from tkinter import *


class Countdown:
    def __init__(self, master):
        self.num = 0
        self.time = None
        self.tk = master
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.tk.geometry("300x300+300+300")
        self.label = Label(self.frame, text="Time={} secs".format(self.num), fg="red")
        self.label.pack(pady=50)
        # Another Frame
        self.frame2 = Frame(self.tk)
        self.frame2.pack(pady=30)
        # Start
        self.button = Button(self.frame2, text="Start", command=self.count)
        self.button.pack(side=LEFT, padx=20)
        # Pause
        self.button2 = Button(self.frame2, text="Pause", command=self.pause)
        self.button2.pack(side=LEFT, padx=20)
        # Stop
        self.button3 = Button(self.frame2, text="Stop", command=self.stop)
        self.button3.pack(side=LEFT, padx=20)

    def count(self):
        self.time = self.tk.after(1000, self.count)
        self.num += 1
        self.label.configure(text="Time={} secs".format(self.num))

    def pause(self):
        self.tk.after_cancel(self.time)

    def stop(self):
        self.tk.after_cancel(self.time)
        self.num = 0
        self.label.configure(text="Time={} secs".format(self.num))


tk = Tk()
c = Countdown(tk)
tk.mainloop()
