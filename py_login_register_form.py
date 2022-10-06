import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
#import mysql.connector
from py_mainform import mainform
import psycopg2

root = Tk()
#connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='py_lg_rg_db')
#conexion = psycopg2.connect(host='localhost',database='aplicada', user='postgresql', password='Martin123')
connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Luis12345',
        database='aplicada'
    )

c = connection.cursor()
#c = conexion.cursor()

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

# ----------- CENTER FORM ------------- #
#   root.overrideredirect(1) # remove border
#   ws = root.winfo_screenwidth()
#   hs = root.winfo_screenheight()
#   x = (ws-w)/2
#   y = (hs-h)/2
#   root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ----------- HEADER ------------- #
hpeque = 100
headerframe = tk.Frame(root, highlightbackgroun= bgcolor, highlightcolor= bgcolor, highlightthickness=2, bg= bgcolor, width=w, height=hpeque)
titleframe = tk.Frame(headerframe, bg= oscuro_color, padx=5, pady=5)
title_label = tk.Label(titleframe, text='SCRUM', padx=100, pady=1, bg= claro_color, fg=tex_oscuro_color, font=('IBM Plex Mono',35), width=8)
buttonframe = tk.Frame(headerframe, bg= oscuro_color, padx=5, pady=5)
close_button = tk.Button(buttonframe, text='Quit', font=('IBM Plex Mono',12))

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
    vals = (username, password)
    select_query = "SELECT * FROM users WHERE username = %s and password = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        #messagebox.showinfo('Test','Test')
        mainformwindow = tk.Toplevel()
        app = mainform(mainformwindow)
        root.withdraw() # hide the root
        mainformwindow.protocol("WM_DELETE_WINDOW", close_win) # close the app

    else:
        messagebox.showwarning('Error','wrong username or password')



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
    title_label['text'] = 'SCRUM'
    title_label['font'] = ('IBM Plex Mono',35)


go_login_label.bind("<Button-1>", lambda page: go_to_login())
# --------------------------------------- #

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM users WHERE username = %s"
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






root.mainloop()


ñl=0
