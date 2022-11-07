import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
#from py_mainform import *
#import py_mainformpro
#import py_mainform
#from py_mainformpro import *
#import mysql.connector
import psycopg2
#import proyectos

root = Tk()
#connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='py_lg_rg_db')
#conexion = psycopg2.connect(host='localhost',database='aplicada', user='postgresql', password='Martin123')
connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Luis12345',
        database='aapp'   #antes aplicada
    )

root.title('ScrumBase')
#root.iconbitmap('s.ico')
c = connection.cursor()
#c = conexion.cursor()


#w = root.winfo_screenwidth()-150
#h = root.winfo_screenheight()-170


w = 1280
h = 720
# background color
bgcolor = "#B6D1CE"

oscuro_color = "#39B29D"
claro_color = "#69CBBF"

tex_oscuro_color = "#364388"
tex_claro_color = "#475499"
tex_superclaro_color = "#686C81"

# ----------- CENTER FORM ------------- #
#root.overrideredirect(1) # remove border
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ----------- HEADER ------------- #

hpeque = 100
headerframe = tk.Frame(root, highlightbackgroun= bgcolor, highlightcolor= bgcolor, highlightthickness=2, bg= bgcolor, width=w, height=hpeque)
titleframe = tk.Frame(headerframe, bg= oscuro_color, padx=5, pady=5)
title_label = tk.Label(titleframe, text='SCRUM', padx=100, pady=1, bg= claro_color, fg=tex_oscuro_color, font=('IBM Plex Mono',35), width=8)
buttonframe = tk.Frame(headerframe, bg= oscuro_color, padx=5, pady=5)
close_button = tk.Button(buttonframe, text='Quit', font=('IBM Plex Mono',10))

headerframe.pack()
titleframe.pack()
title_label.pack()

headerframe.pack()
titleframe.pack()
title_label.pack()
close_button.pack()

titleframe.place(y=50, relx=0.5, anchor=CENTER)  # UBICACIÓN DEL TÍTULO
buttonframe.place(x=1210, y=25)                  # UBICACIÓN DEL BOTÓN

# close window
def close_win():
    root.destroy()

close_button['command'] = close_win
#close_button['command'] = close_win

# ----------- END HEADER ------------- #

mainframe = tk.Frame(root, width=w, height=h)

# ----------- Login Page ------------- #

loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, padx=30, pady=100, highlightbackgroun= oscuro_color, highlightcolor= oscuro_color, highlightthickness=2, bg= bgcolor, width=w, height=h-hpeque)

username_label = tk.Label(login_contentframe, text='Username:', font=('IBM Plex Mono',16), bg= bgcolor,fg = tex_superclaro_color)
password_label = tk.Label(login_contentframe, text='Password:', font=('IBM Plex Mono',16), bg= bgcolor,fg = tex_superclaro_color)

username_entry = tk.Entry(login_contentframe, font=('IBM Plex Mono',16))
password_entry = tk.Entry(login_contentframe, font=('IBM Plex Mono',16), show='*')

login_button = tk.Button(login_contentframe,text="Login", font=('IBM Plex Mono',16), bg=claro_color,fg=tex_oscuro_color, padx=15, pady=5, width=20)

go_register_label = tk.Label(login_contentframe, text=">> don't have an account? create one" , font=('IBM Plex Mono',10), bg= bgcolor, fg='red')

mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

#username_label.grid(row=0, column=2, pady=10)
username_label.place(x=400, y=100)
#username_entry.grid(row=0, column=3)
username_entry.place(x=560, y=100)

#password_label.grid(row=1, column=2, pady=10)
password_label.place(x=400, y=160)
#password_entry.grid(row=1, column=3)
password_entry.place(x=560, y=160)

#login_button.grid(row=2, column=0, columnspan=2, pady=40)
login_button.place(x=460, y=320)

#go_register_label.grid(row=3, column=0, columnspan=2, pady=20)
go_register_label.place(x=500, y=400)

# create a function to display the register frame
def go_to_register():
    loginframe.forget()
    registerframe.pack(fill="both", expand=1)
    title_label['text'] = 'Register'
    title_label['font'] = ('IBM Plex Mono',25)


go_register_label.bind("<Button-1>", lambda page: go_to_register())


# create a function to make the user login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    vals = (username, password,)
    select_query = "SELECT * FROM usuarios WHERE username = %s and password = %s" #antes users
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        #messagebox.showinfo('Test','Test')
        proyectoswindow = tk.Toplevel()
        app = proyectos(proyectoswindow)
        root.withdraw() # hide the root
        proyectoswindow.protocol("WM_DELETE_WINDOW", close_win) # close the app

    else:
        messagebox.showwarning('Error','Usuario o contraseña errada')



login_button['command'] = login


# ----------- Register Page ------------- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, width=w, height=h-hpeque, padx=15, pady=15, highlightbackgroun= oscuro_color, highlightcolor= oscuro_color, highlightthickness=2, bg= bgcolor)

fullname_label_rg = tk.Label(register_contentframe, text='Fullname:', font=('IBM Plex Mono',14), bg= bgcolor,fg = tex_superclaro_color)
username_label_rg = tk.Label(register_contentframe, text='Username:', font=('IBM Plex Mono',14), bg= bgcolor,fg = tex_superclaro_color)
password_label_rg = tk.Label(register_contentframe, text='Password:', font=('IBM Plex Mono',14), bg= bgcolor,fg = tex_superclaro_color)
confirmpass_label_rg = tk.Label(register_contentframe, text='Re-Password:', font=('IBM Plex Mono',14), bg= bgcolor,fg = tex_superclaro_color)
phone_label_rg = tk.Label(register_contentframe, text='Phone:', font=('IBM Plex Mono',14), bg= bgcolor,fg = tex_superclaro_color)
gender_label_rg = tk.Label(register_contentframe, text='Gender:', font=('IBM Plex Mono',14), bg= bgcolor,fg = tex_superclaro_color)




fullname_entry_rg = tk.Entry(register_contentframe, font=('IBM Plex Mono',14), width=22)
username_entry_rg = tk.Entry(register_contentframe, font=('IBM Plex Mono',14), width=22)
password_entry_rg = tk.Entry(register_contentframe, font=('IBM Plex Mono',14), width=22, show='*')
confirmpass_entry_rg = tk.Entry(register_contentframe, font=('IBM Plex Mono',14), width=22, show='*')
phone_entry_rg = tk.Entry(register_contentframe, font=('IBM Plex Mono',14), width=22)

radiosframe = tk.Frame(register_contentframe)
gender = StringVar()
gender.set('Male')
male_radiobutton = tk.Radiobutton(radiosframe, text='Male', font=('IBM Plex Mono',14), bg= bgcolor, variable=gender, value='Male',fg = tex_superclaro_color)
female_radiobutton = tk.Radiobutton(radiosframe, text='Female', font=('IBM Plex Mono',14), bg= bgcolor, variable=gender, value='Female',fg = tex_superclaro_color)


register_button = tk.Button(register_contentframe,text="Register", font=('IBM Plex Mono',14), bg=claro_color,fg=tex_oscuro_color, padx=15, pady=5, width=20)

go_login_label = tk.Label(register_contentframe, text=">> already have an account? sign in" , font=('IBM Plex Mono',10), bg= bgcolor, fg='red')

#mainframe.pack(fill='both', expand=1)
#registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)


fullname_label_rg.place(x=440, y=70)
fullname_entry_rg.place(x=580, y=70)

username_label_rg.place(x=440, y=130)
username_entry_rg.place(x=580, y=130)

password_label_rg.place(x=440, y=180)
password_entry_rg.place(x=580, y=180)

confirmpass_label_rg.place(x=440, y=230)
confirmpass_entry_rg.place(x=580, y=230)

phone_label_rg.place(x=440, y=280)
phone_entry_rg.place(x=580, y=280)

gender_label_rg.place(x=440, y=330)
radiosframe.place(x=625, y=330)
male_radiobutton.grid(row=0, column=0)
female_radiobutton.grid(row=0, column=1)


register_button.place(x=500, y=390)

go_login_label.place(x=520, y=485)

# --------------------------------------- #


# create a function to display the login frame
def go_to_login():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)
    title_label['text'] = 'INICIAR SESIÓN '
    #title_label['bg'] = '#2980b9'


go_login_label.bind("<Button-1>", lambda page: go_to_login())
# --------------------------------------- #

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM usuarios WHERE username = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False



# --------------------------------------- #


# create a function to register a new user
def register():

    fullname = fullname_entry_rg.get().strip() # remove white space
    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    confirm_password = confirmpass_entry_rg.get().strip()
    phone = phone_entry_rg.get().strip()
    gdr = gender.get()
    
    

    if len(fullname) > 0 and  len(username) > 0 and len(password) > 0 and len(phone) > 0:
        if check_username(username) == False: 
            if password == confirm_password:
                vals = (fullname, username, password, phone, gdr)
                insert_query = "INSERT INTO users(fullname, username, password, phone, gender) VALUES (%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Register','your account has been created successfully')
            else:
                messagebox.showwarning('Password','incorrect password confirmation')
        else:
            messagebox.showwarning('Duplicate Username','This Username Already Exists, try another one')
    else:
        messagebox.showwarning('Empty Fields','make sure to enter all the information')

register_button['command'] = register

# --------------------------------------- #

# ------------------------------------------------------------------------ #

class proyectos:

    def __init__ (self, master):


        #cur=py_login_register_form.connection.cursor()
        self.master = master
        w = self.master.winfo_screenwidth()-150
        h = self.master.winfo_screenheight()-170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ------------------------------ #

        self.master.config(bg=bgcolor)
        self.sc = tk.Button (self.master, text= 'Quit', padx=2, pady=1, fg=tex_oscuro_color, font=('IBM Plex Mono',10))
        self.sc.pack()
        self.sc.place(rely=0.04, relx=0.95, anchor=CENTER)
        def close_win():
            root.destroy()

        self.sc['command'] = close_win

        # ------- PROYECTO 1 --------- #

        self.PY1Cua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=350, height=170)
        self.PY1frame = tk.Frame (self.PY1Cua, bg=oscuro_color, padx=5, pady=5)
        self.PY1 = tk.Button (self.PY1frame, text= 'Proyectos', padx=50, pady=5, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color, width=10)
        self.PY1Cua.pack()
        self.PY1frame.pack()
        self.PY1.pack()
        self.PY1Cua.place(rely=0.6, relx=0.333, anchor=CENTER)
        self.PY1frame.place(rely=0.5, relx=0.5, anchor=CENTER)

        # ------- PROYECTO 2 --------- #

        self.PY2Cua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=350, height=170)
        self.PY2frame = tk.Frame (self.PY2Cua, bg=oscuro_color, padx=5, pady=5)
        self.PY2 = tk.Button (self.PY2frame, text= 'Crear', padx=50, pady=5, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color, width=10)
        self.PY2Cua.pack()
        self.PY2frame.pack()
        self.PY2.pack()
        self.PY2Cua.place(rely=0.6, relx=0.666, anchor=CENTER)
        self.PY2frame.place(rely=0.5, relx=0.5, anchor=CENTER)

        # ------- PROYECTOS -------- #

        self.PY3Cua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightthickness=2, bg=claro_color, width=450, height=170)
        self.PY3frame = tk.Frame (self.PY3Cua, bg=oscuro_color, padx=5, pady=5)
        self.PY3 = tk.Label (self.PY3frame, text= ' Home Page ', padx=50, pady=5, fg=tex_oscuro_color, font=('IBM Plex Mono',35), width=10,bg = claro_color)
        self.PY3Cua.pack()
        self.PY3frame.pack()
        self.PY3.pack()
        self.PY3Cua.place(rely=0.2, relx=0.5, anchor=CENTER)
        self.PY3frame.place(rely=0.5, relx=0.5, anchor=CENTER)


        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = sb(scrumwindow)
    

        
        self.PY1['command'] = scrumsalto
        self.PY2['command'] = scrumsalto
    #    self.PY3['command'] = scrumsalto


class sb:

    def __init__(self, master):

        self.master = master
        w = self.master.winfo_screenwidth()-150
        h = self.master.winfo_screenheight()-170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.master.config(bg=bgcolor)
        self.sc = tk.Button (self.master, text= 'Quit', padx=2, pady=1, fg=tex_oscuro_color, font=('IBM Plex Mono',10))
        self.sc.pack()
        self.sc.place(rely=0.04, relx=0.95, anchor=CENTER)
        def close_win():
            root.destroy()

        self.sc['command'] = close_win

        # ------- PROYECTO 1 --------- #

        self.PY1Cua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=330, height=170)
        self.PY1frame = tk.Frame (self.PY1Cua, bg=oscuro_color, padx=5, pady=5)
        self.PY1 = tk.Button (self.PY1frame, text= 'To Do', padx=50, pady=5, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color, width=10)
        self.PY1Cua.pack()
        self.PY1frame.pack()
        self.PY1.pack()
        self.PY1Cua.place(rely=0.6, relx=0.25, anchor=CENTER)
        self.PY1frame.place(rely=0.5, relx=0.5, anchor=CENTER)

        # ------- PROYECTO 2 --------- #

        self.PY2Cua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=330, height=170)
        self.PY2frame = tk.Frame (self.PY2Cua, bg=oscuro_color, padx=5, pady=5)
        self.PY2 = tk.Button (self.PY2frame, text= 'In Progress', padx=50, pady=5, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color, width=10)
        self.PY2Cua.pack()
        self.PY2frame.pack()
        self.PY2.pack()
        self.PY2Cua.place(rely=0.6, relx=0.5, anchor=CENTER)
        self.PY2frame.place(rely=0.5, relx=0.5, anchor=CENTER)

                # ------- PROYECTO 2 --------- #

        self.PYNCua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=330, height=170)
        self.PYNframe = tk.Frame (self.PYNCua, bg=oscuro_color, padx=5, pady=5)
        self.PYN = tk.Button (self.PYNframe, text= 'Done', padx=50, pady=5, font=('IBM Plex Mono',23), fg=tex_claro_color, bg=claro_color, width=10)
        self.PYNCua.pack()
        self.PYNframe.pack()
        self.PYN.pack()
        self.PYNCua.place(rely=0.6, relx=0.75, anchor=CENTER)
        self.PYNframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # ------- TITULO -------- #

        self.PY3Cua =tk.Frame (self.master, highlightbackground=oscuro_color, highlightthickness=2, bg=claro_color, width=450, height=170)
        self.PY3frame = tk.Frame (self.PY3Cua, bg=oscuro_color, padx=5, pady=5)
        self.PY3 = tk.Label (self.PY3frame, text= ' Scrum Board ', padx=50, pady=5, fg=tex_oscuro_color, font=('IBM Plex Mono',35), width=10,bg = claro_color)
        self.PY3Cua.pack()
        self.PY3frame.pack()
        self.PY3.pack()
        self.PY3Cua.place(rely=0.2, relx=0.5, anchor=CENTER)
        self.PY3frame.place(rely=0.5, relx=0.5, anchor=CENTER)

                # ------- VOLVER -------- #

        self.volCua =tk.Frame (self.master, highlightbackground=claro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=450, height=800)
        self.volframe = tk.Frame (self.DoneCua, bg=bgcolor, padx=1, pady=1)
        self.vol = tk.Button (self.Doneframe, text= 'VOLVER', padx=50, pady=5, fg='black', font=('IBM Plex Mono',20), width=10)
        self.volCua.pack()
        self.volframe.pack()
        self.vol.pack()
        self.volCua.place(rely=0.8, relx=0.8, anchor=CENTER)
        self.volframe.place(rely=0.4, relx=0.5, anchor=CENTER)

        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.destroy()
            app = todo(scrumwindow)
        
        self.toDo['command'] = scrumsalto

        def scrumsalto2():
            scrumwindow = tk.Toplevel()
            self.master.destroy()
            app = progress(scrumwindow)
        
        self.InPro['command'] = scrumsalto2

        def scrumsalto3():
            scrumwindow = tk.Toplevel()
            self.master.destroy()
            app = done(scrumwindow)
        
        self.Done['command'] = scrumsalto3

        def scrumsalto4():
            scrumwindow = tk.Toplevel()
            self.master.destroy()
            #app = done(scrumwindow)
            app = proyectos(scrumwindow)
        
        self.vol['command'] = scrumsalto4       

class todo:

    def __init__(self, master):
        
#        connection = psycopg2.connect(
#        host='localhost',
#        user='postgres',
#        password='Martin123',
#        database='prueba'
#        )
     #   c=py_login_register_form.connection.cursor()
        #c = connection.cursor()
        #select_query = "SELECT * FROM users"
        consulta = "consultasss"
     #   consulta=c.execute(select_query)
        #onnection.commit()
        #self.ToDoEspa = tk.Frame (self.ToDoCua, bg=bgcolor, padx=1, pady=1)
        #self.ToDoEspa1 = tk.Label (self.ToDoEspa, text= ' HISTORIA DE ECM ', padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)

        self.master = master
        w = self.master.winfo_screenwidth()-150
        h = self.master.winfo_screenheight()-170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.master.config(bg=bgcolor)
        self.sc = tk.Button (self.master, text= 'Quit', padx=2, pady=1, fg=tex_oscuro_color, font=('IBM Plex Mono',10))
        self.sc.pack()
        self.sc.place(rely=0.04, relx=0.95, anchor=CENTER)
        def close_win():
            root.destroy()

        self.sc['command'] = close_win

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg=bgcolor)

        # -------- TITULO -------------- #

        self.header = tk.Frame (self.master, highlightbackground=bgcolor, highlightcolor=bgcolor, highlightthickness=2, bg=bgcolor, width=ws, height=70)
        self.titleframe = tk.Frame(self.header, bg=bgcolor, padx=1, pady=1)
        self.lbl = tk.Label(self.titleframe, text=' SCRUM BOARD ', padx=50, pady=5, fg='black', font=('IBM Plex Mono',20), width=10)
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TO DO ------------- #

        self.ToDoCua =tk.Frame (self.master, highlightbackground=claro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=ws-250, height=800)
        self.ToDoframe = tk.Frame (self.ToDoCua, bg=bgcolor, padx=1, pady=1)
        self.toDo = tk.Label (self.ToDoframe, text= ' TO DO ', padx=50, pady=5, fg='black', font=('IBM Plex Mono',25), width=10)
        self.ToDoEspa = tk.Frame (self.ToDoCua, bg=bgcolor, padx=1, pady=1)
        self.ToDoEspa1 = tk.Label (self.ToDoEspa, text= str(consulta), padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)
        self.ToDoEspa2 = tk.Frame (self.ToDoCua, bg=bgcolor, padx=1, pady=1)
        self.ToDoEspa3 = tk.Label (self.ToDoEspa2, text= ' HISTORIA DE USUARIO 2 ', padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)
        self.ToDoCua.pack()
        self.ToDoframe.pack()
        self.toDo.pack()
        self.ToDoEspa.pack()
        self.ToDoEspa1.pack()
        self.ToDoEspa2.pack()
        self.ToDoEspa3.pack()
        self.ToDoCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.ToDoframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.ToDoEspa.place(rely=0.4, relx=0.3, anchor=CENTER)
        self.ToDoEspa2.place(rely=0.4, relx=0.7, anchor=CENTER)

class progress:

    def __init__(self, master):
        
        self.master = master
        w = self.master.winfo_screenwidth()-150
        h = self.master.winfo_screenheight()-170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.master.config(bg=bgcolor)
        self.sc = tk.Button (self.master, text= 'Quit', padx=2, pady=1, fg=tex_oscuro_color, font=('IBM Plex Mono',10))
        self.sc.pack()
        self.sc.place(rely=0.04, relx=0.95, anchor=CENTER)
        def close_win():
            root.destroy()

        self.sc['command'] = close_win

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg=bgcolor)

        # -------- TITULO -------------- #

        self.header = tk.Frame (self.master, highlightbackground=bgcolor, highlightcolor=bgcolor, highlightthickness=2, bg=bgcolor, width=ws, height=70)
        self.titleframe = tk.Frame(self.header, bg=bgcolor, padx=1, pady=1)
        self.lbl = tk.Label(self.titleframe, text=' SCRUM BOARD ', padx=50, pady=5, fg='black', font=('IBM Plex Mono',20), width=10)
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TO DO ------------- #

        self.InProCua =tk.Frame (self.master, highlightbackground=claro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=ws-250, height=800)
        self.InProframe = tk.Frame (self.InProCua, bg=bgcolor, padx=1, pady=1)
        self.InPro = tk.Label (self.InProframe, text= ' PROGRESS ', padx=50, pady=5, fg='black', font=('IBM Plex Mono',20), width=10)
        self.InProEspa = tk.Frame (self.InProCua, bg=bgcolor, padx=1, pady=1)
        self.InProEspa1 = tk.Label (self.InProEspa, text= ' EN PROGRESO 1 ', padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)
        self.InProEspa2 = tk.Frame (self.InProCua, bg=bgcolor, padx=1, pady=1)
        self.InProEspa3 = tk.Label (self.InProEspa2, text= ' EN PROGRESO 2 ', padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)
        self.InProCua.pack()
        self.InProframe.pack()
        self.InPro.pack()
        self.InProEspa.pack()
        self.InProEspa1.pack()
        self.InProEspa2.pack()
        self.InProEspa3.pack()
        self.InProCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.InProframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.InProEspa.place(rely=0.4, relx=0.3, anchor=CENTER)
        self.InProEspa2.place(rely=0.4, relx=0.7, anchor=CENTER)

class done:

    def __init__(self, master):
        
        self.master = master
        w = self.master.winfo_screenwidth()-150
        h = self.master.winfo_screenheight()-170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.master.config(bg=bgcolor)
        self.sc = tk.Button (self.master, text= 'Quit', padx=2, pady=1, fg=tex_oscuro_color, font=('IBM Plex Mono',10))
        self.sc.pack()
        self.sc.place(rely=0.04, relx=0.95, anchor=CENTER)
        def close_win():
            root.destroy()

        self.sc['command'] = close_win

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg=bgcolor)

        # -------- TITULO -------------- #

        self.header = tk.Frame (self.master, highlightbackground=bgcolor, highlightcolor=bgcolor, highlightthickness=2, bg=bgcolor, width=ws, height=70)
        self.titleframe = tk.Frame(self.header, bg=bgcolor, padx=1, pady=1)
        self.lbl = tk.Label(self.titleframe, text=' SCRUM BOARD ', padx=50, pady=5, fg='black', font=('IBM Plex Mono',20), width=10)
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TO DO ------------- #

        self.DoneCua =tk.Frame (self.master, highlightbackground=claro_color, highlightcolor=claro_color, highlightthickness=2, bg=claro_color, width=ws-250, height=800)
        self.Doneframe = tk.Frame (self.DoneCua, bg=bgcolor, padx=1, pady=1)
        self.Done = tk.Label (self.Doneframe, text= ' DONE ', padx=50, pady=5, fg='black', font=('IBM Plex Mono',20), width=10)
        self.DoneEspa = tk.Frame (self.DoneCua, bg=bgcolor, padx=1, pady=1)
        self.DoneEspa1 = tk.Label (self.DoneEspa, text= ' TERMINADO 1 ', padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)
        self.DoneEspa2 = tk.Frame (self.DoneCua, bg=bgcolor, padx=1, pady=1)
        self.DoneEspa3 = tk.Label (self.DoneEspa2, text= ' TERMINADO 2 ', padx=150, pady=150, fg='black', font=('IBM Plex Mono',20), width=10)
        self.DoneCua.pack()
        self.Doneframe.pack()
        self.Done.pack()
        self.DoneEspa.pack()
        self.DoneEspa1.pack()
        self.DoneEspa2.pack()
        self.DoneEspa3.pack()
        self.DoneCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.Doneframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.DoneEspa.place(rely=0.4, relx=0.3, anchor=CENTER)
        self.DoneEspa2.place(rely=0.4, relx=0.7, anchor=CENTER)



root.mainloop()