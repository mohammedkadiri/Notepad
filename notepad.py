"""Notepad

This class implements a customised replica of a notepad application including
all the basic functionality of a text-editor program such as Opening files, Editing files,
Formatting and Viewing files.

Author : Mohammed Kadiri
Date : 20 June 2019
"""

from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext


class NotePad(Tk):
    """ NotePad a basic text-editing program which provides functionality such as editing,saving,formating etc."""
    def __init__(self):
        super(NotePad, self).__init__()
        self.geometry("600x515+300+300")
        self.title("Untitled - Notepad")
        self.iconbitmap('icons\\Naruto.ico')
        self.menubar = Menu(self)
        self.file_menu = Menu(self.menubar, tearoff=0, activebackground='black', activeforeground='#2471A3')
        self.edit_menu = Menu(self.menubar, tearoff=0)
        self.format_menu = Menu(self.menubar, tearoff=0)
        self.view_menu = Menu(self.menubar, tearoff=0)
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.create_menu_bar()
        self.create_scroll_wheel()
        self.add_drop_down_menu()
        self.config(menu=self.menubar)

    def create_menu_bar(self):
        """Creates a menu bar for the window."""
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menubar.add_cascade(label="Format", menu=self.format_menu)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)


    def create_scroll_wheel(self):
        """ Include a horizontal-scroll wheel to the window."""
        self.text = scrolledtext.ScrolledText(width=10, height=2, wrap=WORD)
        self.text.config(bg='#273746', fg='#2ECC71')
        self.text.pack(expand=TRUE, fill='both')

    def add_drop_down_menu(self):
        """Provides a cascading drop-down option for each menu."""
        self.file_menu.add_command(label="New")
        self.file_menu.config(bg='#2C3E50', fg='#2ECC71')
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save")
        self.file_menu.add_command(label="Save As...")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Page Setup...")
        self.file_menu.add_command(label="Print")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit")

    def read(self, filepath):
        """ Reads a file and displays to window"""
        self.text.insert('end', open(filepath, 'r').read())

    def open(self):
        """ Display a file dialog to open a file"""
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.read(filename)




notepad = NotePad()
notepad.mainloop()

