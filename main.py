from Tkinter import *
from frame import *

root = Tk()
root.title("Titleless file")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
frame = MainFrame(root,12)
root.mainloop()
