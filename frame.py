from Tkinter import *
from tkFileDialog import *
import webbrowser

class MainFrame:

    root = None
    textArea = None
    fontSize = None

    def __init__(self, root, fontSize):
        self.root = root
        self.fontSize = fontSize
        textFrame = Frame(root)
        scroll = Scrollbar(textFrame)
        scroll.pack(side=RIGHT, fill=Y)
        textArea = Text(textFrame,yscrollcommand=scroll.set,font=("Helvetica", fontSize))
        scroll.config(command=textArea.yview)
        textFrame.pack(fill='both', expand='yes')
        self.textArea = textArea
        self.textArea.pack(fill='both', expand='yes')
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=lambda: self.open_file(textArea))
        filemenu.add_command(label="Save", command=lambda: self.save_file(textArea))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: self.exit(textFrame))
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=lambda: self.about_window(textFrame))
        menubar.add_cascade(label="Help", menu=helpmenu)
        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Zoom +", command=lambda: self.changeTextSize(textFrame,scroll,1))
        viewmenu.add_command(label="Zoom -", command=lambda: self.changeTextSize(textFrame,scroll,-1))
        menubar.add_cascade(label="View", menu=viewmenu)
        root.config(menu=menubar)
        root.bind('<Control-c>', lambda x: self.copy())
        root.bind('<Control-x>', lambda x: self.cut())
        root.bind('<Control-v>', lambda x: self.paste())

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

    def about_window(self,parent):
        top = self.top = Toplevel(parent)
        top.title("Exit")
        file = open("about","r")
        data = file.read()
        l = Label(top, text=data)
        l.pack()
        url = Label(top, text="GitHub Repository", fg="blue", cursor="hand2")
        url.pack()
        url.bind("<Button-1>", lambda x: webbrowser.open_new("https://github.com/DiegoArcelli/TextEditor"))
        parent.wait_window(top)

    def exit(self, parent):
        top = self.top = Toplevel(parent)
        top.title("Exit")
        l = Label(top, text="Are you sure?")
        l.pack(pady=5,padx=5)
        b1 = Button(top, text="Yes", command=self.root.destroy)
        b1.pack(pady=5)
        b2 = Button(top, text="No", command=top.destroy)
        b2.pack(pady=5)
        parent.wait_window(top)

    def copy(self, event=None):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)

    def changeTextSize(self,parent,scroll,val):
        text = self.textArea.get("1.0",END)
        self.textArea.destroy()
        self.fontSize+=val
        self.textArea = Text(parent,yscrollcommand=scroll.set, font=("Helvetica", self.fontSize))
        parent.pack(fill='both', expand='yes')
        parent.pack(fill='both', expand='yes')
        self.textArea.insert(END,text)
        self.textArea.pack(fill='both', expand='yes')
