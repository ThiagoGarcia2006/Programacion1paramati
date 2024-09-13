from funciones_empleados import *

def duplicar(a):
    return a * 2
def mitad(a):
    return a / 2

def pasar_mayuscula(cadena):
    return cadena.upper()

#unaFuncion = pasar_mayuscula

numeros = [3, 45, 2, 3, 66, 42, 5, 56, 67, 4]
nombres = ["Juan", "María", "Luis", "Ana", "Pedro"]

#pares = filtrar_lista(lambda numero: numero % 2 == 0, numeros)
#x = filtrar_lista(lambda numero: numero >= 30 and numero <= 60, numeros)
x = filtrar_lista( lambda nombre: len(nombre) < 5, nombres)


#x = mapear_lista(duplicar, numeros)
#x = mapear_lista(mitad, numeros)
#x = mapear_lista(pasar_mayuscula, nombres)
#x = mapear_lista(unaFuncion, nombres)
#x = mapear_lista(lambda nombre: nombre.upper(), nombres)

#print(pares)
print(x)