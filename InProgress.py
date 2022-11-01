from struct import pack
import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
#import mysql.connector

rootIP = Tk()
rootIP.title("Scrum")

    # close window
def close_win():
    rootIP.destroy()


class mainformIP:

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


    mainframe = tk.Frame(rootIP,bg=bgcolor, width=w, height=h)

    frame_titulo = tk.Frame(mainframe,bg= oscuro_color, padx=8, pady=8)
    label_titulo = tk.Label(frame_titulo, text='IN PROGRESS', padx=60, pady=1, bg= claro_color, fg=tex_oscuro_color, font=('IBM Plex Mono',35))
    frame_quit = tk.Frame(mainframe, bg= oscuro_color, padx=5, pady=5)
    button_quit = tk.Button(frame_quit, text='Quit', font=('IBM Plex Mono',10))
    frame_menu = tk.Frame(mainframe, bg= oscuro_color, padx=5, pady=5)
    button_menu = tk.Button(frame_menu, text='Menu', font=('IBM Plex Mono',10))

    button_quit['command'] = close_win

    mainframe.pack()
    frame_titulo.pack()
    label_titulo.pack()
    frame_quit.pack()
    button_quit.pack()
    frame_menu.pack()
    button_menu.pack()

    frame_titulo.place(y=50, relx=0.5, anchor=CENTER)
    frame_quit.place(x=1210, y=25) 
    frame_menu.place(x=70, y=25)



    
    rootIP.mainloop()