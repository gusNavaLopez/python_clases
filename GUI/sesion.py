from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Inicio de sesion")

marcoPrincipal = ttk.Frame(raiz)
marcoPrincipal.grid(column=0, row=0)

usuario = StringVar
contraseña = StringVar

ttk.Label(marcoPrincipal, text="Usuario: ").grid(column=0, row=0)
ttk.Entry(marcoPrincipal).grid(column=1, row=0)
ttk.Label(marcoPrincipal, text="Contraseña: ").grid(column=0, row=1)
ttk.Entry(marcoPrincipal).grid(column=1, row=1)
ttk.Button(marcoPrincipal, text="Ingresar").grid(column=1,row=2, sticky=E)

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

raiz.mainloop() #Impide que cierre la ventana