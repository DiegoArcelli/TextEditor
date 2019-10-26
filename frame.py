from Tkinter import *
from tkFileDialog import *

class MainFrame:

    def __init__(self, root):
        textFrame = Frame(root)
        scroll = Scrollbar(textFrame)
        scroll.pack(side=RIGHT, fill=Y)
        textArea = Text(textFrame,yscrollcommand=scroll.set)
        scroll.config(command=textArea.yview)
        textFrame.pack(fill='both', expand='yes')
        textArea.pack(fill='both', expand='yes')
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=lambda: self.open_file(textArea))
        filemenu.add_command(label="Save", command=lambda: self.save_file(textArea))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

    def save_file(self,text):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        save = str(text.get(1.0, END))
        f.write(save)
        f.close()

    def open_file(self,text):
        filename = askopenfilename()
        print(filename)
        file = open(filename,"r")
        data = file.read()
        text.delete('1.0', END)
        text.insert(INSERT,data)
