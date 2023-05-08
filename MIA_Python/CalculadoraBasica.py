#importamos una funcion de un archivo de la misma carpeta
from FundamentosPython import nuevoTema
#importa de otra carpeta un archivo indicado
import Calc.Operaciones 
#Sustituimos todo con un nombre determinado para facilitar su llamado
import Calc.Operaciones as C 

if __name__ == "__main__":
    nuevoTema("Modulos y paquetes")
    print("la suma: ", Calc.Operaciones.suma(2, 3))
    print("La resta: ", Calc.Operaciones.resta(20, 3))
    print("----------------------")
    print("la suma: ", C.suma(2, 3))
    print("La resta: ", C.resta(20, 3))