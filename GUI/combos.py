from tkinter import *
from tkinter import ttk

raiz = Tk()

estado = StringVar()
listaEdos = ["Sinaloa", "Nayarit", "Sonora", "Durango", "Jalisco"]
comboEstados = ttk.Combobox(raiz,textvariable=estado)
comboEstados.grid()
comboEstados['values'] = (listaEdos)

raiz.mainloop()