from tkinter import *

# Create a class to represent notepads
#First create the  menu
class Notepad:
    def __init__(self, master):
        self.menubar = Menu(master)
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.edit_menu = Menu(self.menubar, tearoff=0)
        self.format_menu = Menu(self.menubar, tearoff=0)
        self.view_menu = Menu(self.menubar, tearoff=0)
        self.help_menu = Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menubar.add_cascade(label="Format", menu=self.format_menu)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        master.config(menu=self.menubar)


root = Tk()
root.geometry("600x515+300+300")
root.title("Untitled - Notepad")
root.iconbitmap('icons\\Naruto.ico')
notepad = Notepad(root)
root.mainloop()