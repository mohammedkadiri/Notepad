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
import tkinter.messagebox


class NotePad(Tk):
    """ NotePad a basic text-editing program which provides functionality such as editing,saving,formating etc."""
    current_open_file = "no_file"

    def __init__(self):
        super().__init__()
        self.geometry("600x515+300+300")
        self.title("Untitled - Notepad")
        self.iconbitmap('icons\\Naruto.ico')
        self.menubar = Menu(self)
        self.file_menu = Menu(self.menubar, tearoff=0, activebackground='black', activeforeground='#2471A3')
        self.edit_menu = Menu(self.menubar, tearoff=0, activebackground='black', activeforeground='#2471A3')
        self.format_menu = Menu(self.menubar, tearoff=0)
        self.view_menu = Menu(self.menubar, tearoff=0)
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.create_menu_bar()
        self.create_scroll_wheel()
        self.add_drop_down_menu()
        self.config(menu=self.menubar)

    def create_menu_bar(self):
        """ Creates a menu bar for the window."""
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
        """ Provides a cascading drop-down option for each menu."""
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.config(bg='#2C3E50', fg='#2ECC71')
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_fileas)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Page Setup...")
        self.file_menu.add_command(label="Print")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.config(bg='#2C3E50', fg='#2ECC71')
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Paste")
        self.edit_menu.add_command(label="Delete")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All")


    def new_file(self):
        """ Create a new file """
        if not self.text.compare("end-1c", "==", "1.0"):
            if self.current_open_file == 'no_file':
                answer = tkinter.messagebox.askquestion('Notepad', "Do you want to save changes to Untitled ?")
                if answer == 'yes':
                    self.save_fileas()
            else:
                answer = tkinter.messagebox.askquestion('Notepad', "Do you want to save changes to" + self.current_open_file + "?")
                if answer == 'yes':
                    self.save_file()
                    self.create_new()
                if answer == 'no':
                    self.create_new()


    def create_new(self):
        self.title("Untitled - Notepad")
        self.current_open_file = 'no_file'
        self.text.delete(1.0, END)

    def read_file(self, filepath):
        """ Reads a file and displays to window"""
        if self.filepath:
            self.text.insert('end', open(filepath, 'r').read())

    def open_file(self):
        """ Display a file dialog to open a file"""
        self.text.delete(1.0, END)
        self.filepath = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Text Documents", "*.txt"), ("All Files", "*.*")))
        if self.filepath:
            self.current_open_file = self.filepath
            self.read_file(self.filepath)
            filename = self.filepath.split("/")[-1] + " - Notepad"
            self.title(filename)

    def save_fileas(self):
        """ Save a file with provided name"""
        self.filepath = filedialog.asksaveasfile(initialdir="/", title="Select file", filetypes=(("Text Documents", "*.txt"), ("All Files", "*.*")))
        text_to_save = str(self.text.get(1.0, END))
        if self.filepath is None:
            return None
        self.current_open_file = self.filepath.name
        self.filepath.write(text_to_save)
        filename = self.filepath.name.split("/")[-1] + " - Notepad"
        self.filepath.close()
        self.title(filename)

    def save_file(self):
        """ Save a file """
        # Check if the file is new
        if self.current_open_file == "no_file":
            self.save_fileas()
        else:
            with open(self.current_open_file, "w") as file:
                file.write(self.text.get(1.0, END))

    def exit(self):
        self.quit()

notepad = NotePad()
notepad.mainloop()

