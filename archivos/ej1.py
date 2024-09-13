import os
import struct

#numero = 3

#mensaje = "El resultado es " 

path = os.getcwd() #get current working directory
path = os.path.join(path, "archivos/mi_archivo.txt")

print(path)

directorio_actual = os.path.dirname(__file__)
path = os.path.join(directorio_actual, "mi_archivo.txt")

print(directorio_actual)