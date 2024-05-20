
def mostrar_lista(lista:list) -> None:
    for indice in range(len(lista)):
        print(lista[indice], end= " ")
    print()

def cargar_enteros_random(lista:list, cant: int, desde:int, hasta: int)->None:
    from random import randint

    for _ in range(cant):
        lista.append(randint(desde, hasta))

def crear_lista_entero_random(cant: int, desde:int, hasta: int)->list:
    lista = []
    cargar_enteros_random(lista, cant, desde, hasta)
    return lista

def sumar_lista(lista: list)-> int:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def calcular_promedio(lista: list) -> float:
    if len(lista) != 0:
        suma = sumar_lista(lista)
        return suma / len(lista)
    else:
        return 0

def obtener_mayor(lista: list)-> int:
    mayor = max(lista)
    return mayor

def obtener_menor(lista: list)-> int:
    menor = min(lista)
    return menor

def entero_in_lista(lista: list, target: int)-> bool:
    return target in lista

def buscar_entero(lista:list, target: int)-> bool:

    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def contar_entero_lista(lista: list, target:int)-> int:
    contador = 0
    for numero in lista:
        if numero == target:
            contador += 1
    return contador
   
#------------------------------------------------------
# tarea pedir 10 numeros usando una lista y calcular la sumatoria, el promedio, el mayor y cuantas veces esta repetido


CANT = 10
MIN = 1
MAX= 100
#numeros = []
#cargar_enteros_random(numeros, CANT, MIN, MAX)
numeros = crear_lista_entero_random(CANT, MIN, MAX)
mostrar_lista(numeros)

#------------------------------------------------------
# obtener la sumatoria de los numeros de la lista

sumatoria = sum(numeros)
#print(sumatoria)

sumatoria = sumar_lista(numeros)
print(sumatoria)

#------------------------------------------------------
#calcular el promedio de los numeros de la lista

try:
    prom = calcular_promedio(numeros)
    print(prom)
except Exception as ex:
    print(ex)  
#promedio = calcular_promedio(numeros)
#print(promedio)

#------------------------------------------------------
#calcular el mayor de los numeros de la lista

mayor = obtener_mayor(numeros)
print(mayor)

#------------------------------------------------------
#calcular el menor de los numeros de la lista

menor = obtener_menor(numeros)
print(menor)

numero = 20

if(entero_in_lista(numeros, numero)):
    print(f"{numero} esta en la lista")
else:
    print(f"{numero} no esta en la lista")   

indice = buscar_entero(numeros, numero)

if indice != -1:
    print(f"{numero} esta en la lista en el indice {indice}")
else:
    print(f"{numero} no esta en la lista") 


#print(numeros.index(10))
x = 10

cantidad = contar_entero_lista(numeros, x)

print(cantidad)

if cantidad == 0:
    print(f"{x} no esta en la lista")
elif cantidad == 1:
    print(f"{x} esta una vez ")
else:
    print(f"{x} esta {cantidad} veces")    
    






