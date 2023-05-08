from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Ejemplos GUI")

marcoPrincipal = ttk.Frame(raiz)
marcoPrincipal.grid(column=0, row=0)

etqTexto = ttk.Label(raiz, text= "Etiqueta de texto")
etqTexto.grid()

imagen = PhotoImage(file="caritas.png")
imagen2 = PhotoImage(file="buho.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="combinada", compound="bottom")
etqCombinada.grid()
etqCombinada['image'] = imagen2





raiz.mainloop()