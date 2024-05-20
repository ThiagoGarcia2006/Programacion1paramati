from random import randint
from time import sleep

def mostrar_lista(lista:list) -> None: 
    validar_lista(lista)
    
    for indice in range(len(lista)):
        print(lista[indice], end= " ")
    print()

def cargar_enteros_random(lista:list, cant: int, desde:int, hasta: int)->None:
    validar_lista(lista)
    from random import randint

    for _ in range(cant):
        lista.append(randint(desde, hasta))

def crear_lista_entero_random(cant: int, desde:int, hasta: int)->list:
    lista = []
    cargar_enteros_random(lista, cant, desde, hasta)
    return lista

def sumar_lista(lista: list)-> int:
    validar_lista(lista)
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def calcular_promedio(lista: list) -> float:
    validar_lista(lista)
    if len(lista) != 0:
        suma = sumar_lista(lista)
        return suma / len(lista)
    else:
        return 0

def obtener_mayor(lista: list)-> int:
    validar_lista(lista)
    mayor = max(lista)
    return mayor

def obtener_menor(lista: list)-> int:
    validar_lista(lista)
    menor = min(lista)
    return menor

def entero_in_lista(lista: list, target: int)-> bool:
    validar_lista(lista)
    return buscar_entero(lista, target) != -1

def buscar_entero(lista:list, target: int)-> bool:
    validar_lista(lista)

    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def contar_entero_lista(lista: list, target:int)-> int:
    validar_lista(lista)
    contador = 0
    for numero in lista:
        if numero == target:
            contador += 1
    return contador

def validar_lista(lista:list)->None:

    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")

def ordenar_lista_ascendente(lista: list)->None:
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i + 1, tam):
            if lista[i] > lista[j] :
                aux = lista[i]
                lista[i] = lista[j] 
                lista[j] = aux 
 
def ordenar_lista_descendente(lista: list)->None:
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i + 1, tam):
            if lista[i] < lista[j] :
                aux = lista[i]
                lista[i] = lista[j] 
                lista[j] = aux 

def ordenar_lista(lista: list, asc: bool = True)->None:
    validar_lista(lista)
    tam = len(lista)  
    for i in range(tam -1):
        for j in range(i + 1, tam):
            if (asc and lista[i] > lista[j]) or (not asc and lista[i] < lista[j]) :
                aux = lista[i]
                lista[i] = lista[j] 
                lista[j] = aux      
                  
def sorteador(lista: list)->None:
    print(f"El ganador es {lista[randint(0, len(lista)-1)]}")


   
    