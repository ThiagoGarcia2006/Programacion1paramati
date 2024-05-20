from data_warehouse import *
LEGAJO = 0
NOMBRE = 1
GENERO = 2
NOTA_P1 = 3
NOTA_P2 = 4
PROMEDIO = 5

def validar_lista(lista:list)->None:

    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")

def calcular_promedio(a: int, b:int)-> float:
    return(a+b) / 2

def mostrar_alumnos(alumnos: list):
    print("         ***Lista de Alumnos")
    print(" Legajo  Nombre  Genero  NotaP1  NotaP2  Promedio")
    print("-----------------------------------------------")
    for i in range(len(alumnos)):
        mostrar_alumno(alumnos[i])
    print()    

def mostrar_alumno(un_alumno: list):
    print(f"{un_alumno[LEGAJO]} {un_alumno[NOMBRE] :>10} {un_alumno[GENERO]} {un_alumno[NOTA_P1]:2} {un_alumno[NOTA_P2]:2} {un_alumno[PROMEDIO]:5.2f}") 

def entero_in_lista(lista: list, target: int)-> bool:
    return buscar_entero(lista, target) != -1

def buscar_entero(lista:list, target: int)-> bool:

    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def cargar_lista_datos(lista_destino: list, lista_origen: list, cant: int)->None:
    for i in range(cant):
        lista_destino.append(lista_origen[i]) 

def cargar_enteros_random(lista:list, cant: int, desde:int, hasta: int)->None:
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))

def cargar_lista_notas(lista: list, cant: int)->None:
    NOTA_MIN = 0
    NOTA_MAX = 10
    cargar_enteros_random(lista, cant, NOTA_MIN, NOTA_MAX)

def cargar_legajos(lista: list, cant: int)->None:
    from random import randint
    LEGAJO_MIN = 20000
    LEGAJO_MAX = 30000
    for _ in range (cant):
        numero = randint(LEGAJO_MIN, LEGAJO_MAX)
    lista.append(numero)    

def calcular_promedios(lista_1: list, lista_2: list, lista_3: list)->None:
    for i in range(len(lista_1)):
        lista_3.append(calcular_promedio(lista_1[i], lista_2[i]))

def cargar_alumnos_aux(legs, names, genders, notes_P1, notes_P2, proms, cant):
    from data_warehouse import nombres, generos
    cargar_legajos(legs, cant)
    cargar_lista_datos(names, nombres, cant)
    cargar_lista_datos(genders, generos, cant)
    cargar_lista_notas(notes_P1, cant)
    cargar_lista_notas(notes_P2, cant)
    calcular_promedios(notes_P1, notes_P2, proms)

def cargar_alumnos(alumnos: list, cant: int)->None:
    from data_warehouse import nombres, generos
    legs = []
    names = []
    genders = []
    notes_P1 = []
    notes_P2 = []
    proms = []
    cargar_legajos(legs, cant)
    cargar_lista_datos(names, nombres, cant)
    cargar_lista_datos(genders, generos, cant)
    cargar_lista_notas(notes_P1, cant)
    cargar_lista_notas(notes_P2, cant)
    calcular_promedios(notes_P1, notes_P2, proms)
    for i in range(cant):
        alumno = []
        alumno.append(legs[i])
        alumno.append(names[i])
        alumno.append(genders[i])
        alumno.append(notes_P1[i])
        alumno.append(notes_P2[i])
        alumno.append(proms[i])
        alumno.append(alumno)

def swap_lista(lista: list, i:int, j:int)->None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_alumnos(legs, names, genders, notes_P1, notes_P2, proms):
    tam = len(legs)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if proms[i] < proms[j]:
                swap_lista(legs, i, j)
                swap_lista(names, i, j)
                swap_lista(genders, i, j)
                swap_lista(notes_P1, i, j)
                swap_lista(notes_P2, i, j)
                swap_lista(proms, i, j)
            

                
