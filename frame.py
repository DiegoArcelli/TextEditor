import tkinter as tk
import tkinter.filedialog as fd
import webbrowser as wb

class MainFrame:

    root = None
    textArea = None
    fontSize = None
    openedFile = None

    def __init__(self, root, fontSize):
        self.root = root
        self.fontSize = fontSize
        self.openedFile = None
        textFrame = tk.Frame(root)
        scroll = tk.Scrollbar(textFrame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        textArea = tk.Text(textFrame,yscrollcommand=scroll.set,font=("Helvetica", fontSize))
        scroll.config(command=textArea.yview)
        textFrame.pack(fill='both', expand='yes')
        self.textArea = textArea
        self.textArea.pack(fill='both', expand='yes')
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=lambda: self.open_file(textArea))
        filemenu.add_command(label="Save", command=lambda: self.save_file(textArea))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: self.exit(textFrame))
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy", command=lambda: self.textArea.event_generate("<<Copy>>"))
        editmenu.add_command(label="Cut", command=lambda: self.textArea.event_generate("<<Cut>>"))
        editmenu.add_command(label="Paste", command=lambda: self.textArea.event_generate("<<Paste>>"))
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=lambda: self.about_window(textFrame))
        helpmenu.add_command(label="Shortcuts", command=lambda: self.shortcuts_window(textFrame))
        menubar.add_cascade(label="Help", menu=helpmenu)
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Zoom +", command=lambda: self.changeTextSize(textFrame,scroll,1))
        viewmenu.add_command(label="Zoom -", command=lambda: self.changeTextSize(textFrame,scroll,-1))
        menubar.add_cascade(label="View", menu=viewmenu)
        root.config(menu=menubar)
        root.bind('<Control-o>', lambda e: self.open_file(textArea))
        root.bind('<Control-O>', lambda e: self.open_file(textArea))
        root.bind('<Control-s>', lambda e: self.save_file(textArea))
        root.bind('<Control-S>', lambda e: self.save_file(textArea))
        root.bind('<Control-plus>', lambda e: self.changeTextSize(textFrame,scroll,1))
        root.bind('<Control-minus>', lambda e: self.changeTextSize(textFrame,scroll,-1))
        root.bind('<Control-a>', lambda e: self.select_all())
        root.bind('<Control-A>', lambda e: self.select_all())
        root.bind('<Control-e>', lambda e: self.exit(textFrame))
        root.bind('<Control-E>', lambda e: self.exit(textFrame))
        root.bind('<Control-H>', lambda e: self.about_window(textFrame))
        root.bind('<Control-h>', lambda e: self.about_window(textFrame))
        root.bind('<Control-l>', lambda e: self.shortcuts_window(textFrame))
        root.bind('<Control-L>', lambda e: self.shortcuts_window(textFrame))

    def save_file(self,text):
        if self.openedFile == None:
            f = fd.asksaveasfile(mode='w')
            if f is None:
                return
            save = str(text.get(1.0, fd.END))
            f.write(save)
            f.close()
        else:
            save = str(text.get(1.0, fd.END))
            f = open(self.openedFile, "w")
            f.write(save)
            f.close()

    def open_file(self,text):
        filename = fd.askopenfilename()
        self.openedFile = filename
        file = open(filename,"r")
        data = file.read()
        text.delete('1.0', fd.END)
        text.insert(fd.INSERT,data)
        obj = filename.split("/")
        self.root.title(obj[len(obj)-1])

    def about_window(self,parent):
        top = self.top = fd.Toplevel(parent)
        top.title("About")
        top.resizable(width=False, height=False)
        file = open("about","r")
        data = file.read()
        l = tk.Label(top, text=data)
        l.grid(row = 0, pady = (5,0), padx = (5,5))
        url = tk.Label(top, text="GitHub Repository", fg="blue", cursor="hand2", height=5, width=20)
        url.grid(row = 1, pady = (0,0), padx = (0,0))
        url.bind("<Button-1>", lambda x: wb.open_new("https://github.com/DiegoArcelli/TextEditor"))
        parent.wait_window(top)

    def shortcuts_window(self,parent):
        top = self.top = fd.Toplevel(parent)
        top.title("Shortcuts")
        file = open("shorts","r")
        data = file.read()
        l = tk.Label(top, text=data, anchor = tk.SW, justify = tk.LEFT, padx = 20, pady = 15)
        l.pack()
        top.resizable(width=False, height=False)

    def exit(self, parent):
        top = self.top = fd.Toplevel(parent)
        top.title("Exit")
        top.resizable(width=False, height=False)
        l = tk.Label(top, text="Are you sure?")
        l.grid(row = 0, columnspan = 2, pady = (10,10), padx = (10,10))
        b1 = tk.Button(top, text="Yes", command=self.root.destroy)
        b1.grid(column = 0, row = 1, pady = (10,10), padx = (10,10))
        b2 = tk.Button(top, text="No", command=top.destroy)
        b2.grid(column = 1, row = 1, pady = (10,10), padx = (10,10))
        parent.wait_window(top)

    def select_all(self):
        self.textArea.tag_add(fd.SEL, "1.0", fd.END)
        self.textArea.mark_set(fd.INSERT, "1.0")
        self.textArea.see(fd.INSERT)

    def changeTextSize(self,parent,scroll,val):
        if self.fontSize > 8 and self.fontSize < 51:
            text = self.textArea.get("1.0",fd.END)
            self.textArea.destroy()
            self.fontSize+=val
            self.textArea = tk.Text(parent, yscrollcommand=scroll.set, font=("Helvetica", self.fontSize))
            parent.pack(fill='both', expand='yes')
            parent.pack(fill='both', expand='yes')
            self.textArea.insert(fd.END,text)
            self.textArea.pack(fill='both', expand='yes')
        elif self.fontSize == 8:
            self.fontSize += 1
        elif self.fontSize == 51:
            self.fontSize -= 1
