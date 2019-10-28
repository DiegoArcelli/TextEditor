from Tkinter import *

class Dialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.title("About")
        l = Label(top, text="Simple text editor")
        l.pack(pady=5,padx=5)
        b = Button(top, text="Close", command=self.close)
        b.pack(pady=5)

    def close(self):
        self.top.destroy()
