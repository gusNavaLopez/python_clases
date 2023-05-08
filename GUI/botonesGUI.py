from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text="Boton de texto")
boton.grid()

imagen = PhotoImage(file="caritas.png")
imagen2 = PhotoImage(file="buho.png")

btnImage = ttk.Button(raiz)
btnImage.grid()
btnImage['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Boton combinado", image=imagen2)
btnCombinada.grid()

chkBoton = ttk.Checkbutton(raiz, text="Check boton")
chkBoton.grid()

rBoton = StringVar()
primer = ttk.Radiobutton(raiz, text="Opcion 1", variable=rBoton, value="primer")
primer.grid()
segunda = ttk.Radiobutton(raiz, text="Opcion 2", variable=rBoton, value="segundo")
segunda.grid()
tercer = ttk.Radiobutton(raiz, text="Opcion 3", variable=rBoton, value="tercero")
tercer.grid()

raiz.mainloop()