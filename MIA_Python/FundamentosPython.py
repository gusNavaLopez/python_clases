def nuevoTema (tema):
    print("\n--------" , tema , "------------" )

if __name__ == "__main__":
    #Este es un comentario suimple
    '''Este es un comentario
    de varias lineas'''
    nuevoTema("Operadores Aritmeticos")
    print("Operador suma, 5 + 3 = ", 5 + 3)
    print("Operador resta, 5 - 3 = ", 5 - 3)
    print("Operador multiplicacion, 5 * 3 = ", 5 * 3)
    print("Operador division, 5 / 3 = ", 5 / 3)
    print("Operador division entera, 5 // 3 = ", 5 // 3)
    print("Operador modulo, 5 % 3 = ", 5 % 3)
    print("Operador cambio de signo, -5 ", -5)
    print("Operador exponente, 5 ** 3 =", 5 ** 3)
    nuevoTema("Operadorres Logicos")
    print("Operador and ")
    print("True and True: ", True and True)
    print("True and False: ", True and False)
    print("False and True: ", False and True)
    print("False and False: ", False and False)
    print("Operador or")
    print("True or True: ", True or True)
    print("True or False: ", True or False)
    print("False or True: ", False or True)
    print("False or False: ", False or False)
    print("Operador not")
    print("Not True: ", not True)
    print("Not False: ", not False)
    nuevoTema("Operadorres Comparacion")
    print("Operador 5 == 5: ", 5 == 5)
    print("Operador 5 != 6: ", 5 != 6)
    print("Operador 5 < 6: ", 5 < 6)
    print("Operador 5 <= 5: ", 5 <= 5)
    print("Operador 6 > 5: ", 6 > 5)
    print("Operador 5 >= 5: ", 5 >= 5)
    nuevoTema("Variables")
    variable1 = 10 #Se declara al escribir el nombre y el valor sin definir tipo
    _variable2 = 6.15
    Variable3 = "Pepe"
    nombreVariable = 8
    nombre_variable = 34.2
    print(variable1,"\n", _variable2,"\n", Variable3, "\n", nombreVariable, "\n", nombre_variable)

    a, b, c = 5, 10.8, "Hola"
    print(a)
    print(b)
    print(c)

    nuevoTema("Enteros")
    w = 105
    x = 1234456789876554321
    y = -75
    z = 0b10011001
    h = 0x34fa
    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("Flotantes")
    x = 123.456
    print(x,type(x))
    y = -34.97823
    print(y,type(y))

    nuevoTema("Numeros Complejos")
    x = -35j
    y = 12 + 67j
    z = 3j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Booleanos")
    lis = []
    print(lis, "is", bool(lis))

    nuevoTema("Listas")
    a =[10, 45.67, "Lista prueba"]
    print(a, type(a))
    print(a[2], type(a[2]))

    nuevoTema("Tuplas")
    t = (3, "tuplas", 3 - 4.6j, 3, 4, 5)
    print(t, type(t))
    print(t[2], type(t[2]))
    print("t[1:5] = ",t[1:5])
    #t[1] = "Tuplas nuevas"
    #print(t)

    nuevoTema("Cadenas")
    cadena = "- Esta es una cadena de caracteres"
    cadena1 = '- Esta cadena lleva comilla sencilla'
    cadena2 = '''- Esta es una
        cadena con 
        salto de linea'''
    print(cadena)
    print(cadena1)
    print(cadena2)
    print(cadena[12])

    nuevoTema("Conjuntos")
    #no tienen un orden especifico y no pueden repetirse
    x = 13
    y = 10
    conjunto = {10,20,30,40,10,50,"hola",x,y}
    print (conjunto,type(conjunto))

    nuevoTema("Diccionario")
    diccionario = {"1":'hola', 
                "nombre":"Gustavo", 
                "edad":31}
    print(diccionario, type[diccionario])
    print("Su edad es: ",diccionario['edad'],"años")
    print(diccionario["1"])