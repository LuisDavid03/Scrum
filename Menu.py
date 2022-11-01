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


class mainformMENU:

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

    frame_titulo = tk.Frame(mainframe,bg= oscuro_color, padx=12, pady=12)
    label_titulo = tk.Label(frame_titulo, text='MENU', padx=100, pady=1, bg= claro_color, fg=tex_oscuro_color, font=('IBM Plex Mono',35))
    frame_quit = tk.Frame(mainframe, bg= oscuro_color, padx=5, pady=5)
    button_quit = tk.Button(frame_quit, text='Quit', font=('IBM Plex Mono',10))


    

    frame_to_do = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_to_do = tk.Button(frame_to_do, text='TO DO', pady=15,padx=68, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color)
    frame_in_progress = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_in_progress = tk.Button(frame_in_progress, text='IN PROGRESS', pady= 15,padx=8, font=('IBM Plex Mono', 23), fg=tex_claro_color, bg=claro_color)
    frame_done = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_done = tk.Button(frame_done, text='DONE', pady= 15,padx=72, font=('IBM Plex Mono', 23), fg=tex_claro_color, bg=claro_color)
    frame_SCRUMBoard = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_SRCUMBoard = tk.Button(frame_SCRUMBoard, text='SCRUM BOARD', pady= 15, font=('IBM Plex Mono', 23), fg=tex_claro_color, bg=claro_color)
    frame_LogOut = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_LogOut = tk.Button(frame_LogOut, text='Log out', pady= 15,padx=66, font=('IBM Plex Mono', 23), fg=tex_claro_color, bg=claro_color)


    button_quit['command'] = close_win

    mainframe.pack()
    frame_titulo.pack()
    label_titulo.pack()
    frame_quit.pack()
    button_quit.pack()
    button_to_do.pack()
    button_in_progress.pack()
    button_done.pack()
    button_SRCUMBoard.pack()
    button_LogOut.pack()


    frame_titulo.place(y=50, relx=0.5, anchor=CENTER)
    frame_quit.place(x=1210, y=25) 
    frame_to_do.place(y=300, relx=0.25, anchor=CENTER)  
    frame_in_progress.place(y=300, relx=0.5, anchor=CENTER) 
    frame_done.place(y=300, relx=0.75, anchor=CENTER)
    frame_SCRUMBoard.place(y=500, relx=0.33, anchor=CENTER)
    frame_LogOut.place(y=500, relx=0.66, anchor=CENTER)


    
    rootIP.mainloop()