import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (ListaProyect, Proyectos, Registroproyect, Registroemp):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(ListaProyect)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class ListaProyect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Proyecto", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 100, pady = 100)

		button1 = ttk.Button(self, text ="Visualizar proyectos en curso",
		command = lambda : controller.show_frame(Proyectos))

		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 100, pady = 100)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Empezar nuevo proyecto",
		command = lambda : controller.show_frame(Registroproyect))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 5, padx = 100, pady = 100)

		button3 = ttk.Button(self, text ="Lista de empleados",
		command = lambda : controller.show_frame(Registroemp))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 1, column = 10, padx = 100, pady = 100)


class Proyectos(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Proyecto", font = LARGEFONT)
		label.grid(row = 2, column = 4, padx = 10, pady = 10)
		button1 = ttk.Button(self, text ="Atras",
		command = lambda : controller.show_frame(PageManager))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

class Registroproyect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Nombre del Nuevo Proyecto", font = LARGEFONT)
		label.grid(row = 2, column = 4, padx = 10, pady = 10)
		button1 = ttk.Button(self, text ="Atras",
		command = lambda : controller.show_frame(PageManager))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

class Registroemp(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="EMPLEADOS", font = LARGEFONT)
		label.grid(row = 2, column = 4, padx = 10, pady = 10)
		button1 = ttk.Button(self, text ="Atras",
		command = lambda : controller.show_frame(PageManager))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
