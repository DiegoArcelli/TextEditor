from Tkinter import *
from frame import *

root = Tk()
root.title("Text Editor")
root.geometry()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
frame = MainFrame(root)
root.mainloop()
