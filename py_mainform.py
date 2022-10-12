# main form
import tkinter as tk
from tkinter import *

# width and height
w = 1280
h = 720
# background color
bgcolor = "#B6D1CE"

oscuro_color = "#39B29D"
claro_color = "#69CBBF"

tex_oscuro_color = "#364388"
tex_claro_color = "#475499"
tex_superclaro_color = "#686C81"

class mainform:
    def __init__(self, master):
        self.master = master
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Add")
        self.products.add_command(label="Edit")
        self.products.add_command(label="Remove")

        self.menubar.add_cascade(menu=self.products, label="Product")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Add")
        self.categories.add_command(label="Edit")
        self.categories.add_command(label="Remove")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()
        

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg="#ecf0f1")
        self.lbl = tk.Button(self.master, text='Form', font=('IBM Plex Mono',45, 'bold'), fg=tex_oscuro_color,bg=bgcolor)
        self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)

        self.lbl.pack()