import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
#import mysql.connector

root = Tk()
root.title("Scrum")

    # close window
def close_win():
    root.destroy()

class mainform:
    
    root = Tk()
    root.title("Scrum")
        # close window
    def close_win():
        root.destroy()

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


    mainframe = tk.Frame(root,bg=bgcolor, width=w, height=h)

    frame_titulo = tk.Frame(mainframe,bg= oscuro_color, padx=8, pady=8)
    label_titulo = tk.Label(frame_titulo, text='Homepage', padx=100, pady=1, bg= claro_color, fg=tex_oscuro_color, font=('IBM Plex Mono',25))
    frame_quit = tk.Frame(mainframe, bg= oscuro_color, padx=5, pady=5)
    button_quit = tk.Button(frame_quit, text='Quit', font=('IBM Plex Mono',10))
    frame_proyectos = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_proyectos = tk.Button(frame_proyectos, text='Proyectos', pady=20, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color)
    frame_crear = tk.Frame(mainframe, bg= oscuro_color, padx=4, pady=4)
    button_crear = tk.Button(frame_crear, text='Crear', pady= 20,padx=34, font=('IBM Plex Mono', 23), fg=tex_claro_color, bg=claro_color)



    button_quit['command'] = close_win

    mainframe.pack()
    frame_titulo.pack()
    label_titulo.pack()
    frame_quit.pack()
    button_quit.pack()
    button_proyectos.pack()
    button_crear.pack()

    frame_titulo.place(y=50, relx=0.5, anchor=CENTER)
    frame_quit.place(x=1210, y=25) 
    frame_proyectos.place(x=350, y=380)  
    frame_crear.place(x=770, y=380) 



    
    root.mainloop()