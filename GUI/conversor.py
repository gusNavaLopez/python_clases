from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
        resultado = round((float(pies.get()) * 0.3048),4) #convierte el valor en float
        metros.set(resultado)
    except ValueError:
        metros.set("Introduce numero")

raiz = Tk() #Es un objeto (Una ventana)
raiz.title("Pies a metros")
#raiz.geometry("500x200")

#Creacion de objetos clases------------------------------------------------
marcoPrincipal = ttk.Frame(raiz, padding="14 14 14 14") #Es un marco que se pone en raiz
marcoPrincipal.grid(column=0, row=0) #Le damos la posicion

pies = StringVar()
metros = StringVar()

#Creacion de elemntos------------------------------------------------
txtPies = ttk.Entry(marcoPrincipal, textvariable=pies, justify="center") #Es un entrada de texto se lo agregamos a la variable
txtPies.grid(column=1, row=0)

#Es un elemnto anonimo, agregando puntos agregas caracteristicas
#grid-indica la ubicacion en el frame, sticky-indica la posicion en su columna(N,S,E,W)
ttk.Label(marcoPrincipal, text="Pies").grid(column=2, row=0)
ttk.Label(marcoPrincipal, text="Son equivalentes a: ").grid(column=0, row=1)
ttk.Label(marcoPrincipal, text="metros").grid(column=2, row=1)
ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1)
#Boton, command=accion al presionar (calcular es funcion)
ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=2, row=2)

#Recorremos cada hijo de marcoprincipal para agregar el pad a todos
for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

#Para al empezar este directo donde escribes
txtPies.focus()
#Para que calcule con "enter"
raiz.bind("<Return>", calcular)#cuando presiones esa tecla, ejecutas la funcion

raiz.mainloop() #Impide que cierre la ventana