import pickle

info = [35, 77, 23, 54, 3.7]

with open("ArchivoSerial", "wb") as binFile:
    pickle.dump(info, binFile)

print("Archivo binario escrito")

with open("ArchivoSerial", "rb") as binFile:
    lista = pickle.load(binFile)
    print(lista)