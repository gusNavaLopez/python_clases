from tkinter import *
from tkinter import ttk

raiz = Tk ()
raiz.title("Muestra Widgets")

marcoPrincipal = ttk.Frame(raiz)
marcoPrincipal.grid(column=0, row=0)

marcoDatos = ttk.Frame(marcoPrincipal)
marcoDatos.grid(column=0, row=0)
marcoDatos.config(relief="raised") #flat, groove, raised, ridge, solid, or sunken
ttk.Label(marcoDatos, text="Nombre: ").grid(column=0, row=0)
ttk.Entry(marcoDatos).grid(column=1,row=0)
ttk.Label(marcoDatos, text="A paterno: ").grid(column=0, row=1)
ttk.Entry(marcoDatos).grid(column=1,row=1)
ttk.Label(marcoDatos, text="A. Materno: ").grid(column=0, row=2)
ttk.Entry(marcoDatos).grid(column=1,row=2)
ttk.Label(marcoDatos, text="Correo: ").grid(column=0, row=3)
ttk.Entry(marcoDatos).grid(column=1,row=3)
ttk.Label(marcoDatos, text="Movil: ").grid(column=0, row=4)
ttk.Entry(marcoDatos).grid(column=1,row=4)

for hijo in marcoDatos.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

ocupacion = StringVar()
marcoOcupacion = ttk.Frame(marcoPrincipal)
marcoOcupacion.grid(column=3, row=0)
estudiante = ttk.Radiobutton(marcoOcupacion, text="Estudiante", variable=ocupacion, value="estudiante").grid(column=0, row=0, sticky=W)
empleado = ttk.Radiobutton(marcoOcupacion, text="Empleado", variable=ocupacion, value="empleado").grid(column=0, row=1, sticky=W)
desempleado = ttk.Radiobutton(marcoOcupacion, text="Desempelado", variable=ocupacion, value="desempleado").grid(column=0, row=2, sticky=W)

marcoAficion = ttk.Frame(marcoPrincipal)
marcoAficion.grid(column=0,row=1)
marcoAficion.config(relief="raised") #flat, groove, raised, ridge, solid, or sunken
ttk.Label(marcoAficion, text="Aficiones:").grid(column=0, row=0)
ttk.Checkbutton(marcoAficion, text="Leer").grid(column=0, row=1)
ttk.Checkbutton(marcoAficion, text="Musica").grid(column=1, row=1)
ttk.Checkbutton(marcoAficion, text="Videojuegos").grid(column=2, row=1)
for hijo in marcoAficion.winfo_children():
    hijo.grid_configure(padx=10, pady=3)

estados = StringVar()
listaEdos = ["Sinaloa", "Nayarit", "Sonora", "Durango", "Jalisco"]
marcoEstado = ttk.Frame(marcoPrincipal)
marcoEstado.grid(column=3, row=1)
comboEstado = ttk.Combobox(marcoEstado, textvariable=estados)
comboEstado.grid(column=0, row=0)
comboEstado['values'] = (listaEdos)
comboEstado.current(0)

marcoBotones = ttk.Frame(marcoPrincipal)
marcoBotones.grid(column=0, row=2, sticky=W)
ttk.Button(marcoBotones, text="Guardar").grid(column=0, row=0, sticky=W)
ttk.Button(marcoBotones, text="Cancelar").grid(column=2, row=0, sticky=E, padx=50)

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)


raiz.mainloop()