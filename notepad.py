"""Notepad

This class implements a customised replica of a notepad application including
all the basic functunality such as Opening files, Editing files,
Formatting and Viewing files.

Author : Mohammed Kadiri
Date : 20 June 2019
"""

from tkinter import *
from tkinter import scrolledtext


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

        # Implement text widget with scrolling comptability

        self.text = scrolledtext.ScrolledText(master, width=10, height=2, wrap=WORD)
        self.text.pack(expand=TRUE, fill='both')

        # Include Dropdown options for File
        self.file_menu.add_command(label="New")
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Save")
        self.file_menu.add_command(label="Save As...")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Page Setup...")
        self.file_menu.add_command(label="Print")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit")

        master.config(menu=self.menubar)



root = Tk()
root.geometry("600x515+300+300")
root.title("Untitled - Notepad")
root.iconbitmap('icons\\Naruto.ico')
notepad = Notepad(root)
root.mainloop()