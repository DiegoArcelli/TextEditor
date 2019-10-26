from Tkinter import *

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
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy", command=MainFrame.copyText(textArea))
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

    def copyText(text):
        copied = text.selection_get()
        print(copied)
