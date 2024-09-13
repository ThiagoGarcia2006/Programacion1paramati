from data_empleados import *
from random import randint, choice

def cargar_lista_empleados_random(lista:list, cantidad:int)->None:
    next_legajo = 20000
    for _ in range(cantidad):
        EDAD_MIN = 18
        EDAD_MAX = 65
        legajo = next_legajo
        next_legajo += 1
        genero = choice(["f", "m"])
        nombre = choice(nombres_m) if genero == "m" else choice(nombres_f)
        apellido = choice(apellidos)
        edad = randint(EDAD_MIN, EDAD_MAX)
        calle = f"calle {randint(10, 99)} nro{randint(100, 999)}"
        localidad = choice(localidades)
        provincia = choice(provincias)
        email = f"{nombre.lower()+ apellido.lower()}{choice(dominios)}"
        sector = choice(sectores)
        sueldo = float(randint(20000, 50000))
        lista.append(new_empleado(legajo, nombre, apellido, genero, edad, calle, localidad, provincia, email,sector,  sueldo))
        
def promedio_campo_sector(lista: list):
    pass

def new_empleado(legajo: int, nombre:str, apellido:str, genero:str, edad:int, calle:str, localidad:str, provincia:str, email:str,sector:str,  sueldo:float)->dict:
    empleados = {}
    empleados["legajo"] = legajo
    empleados["nombre"] = nombre
    empleados["apellido"] = apellido
    empleados["genero"] = genero
    empleados["edad"] = edad
    empleados["calle"] = calle
    empleados["localidad"] = localidad
    empleados["provincia"] = provincia
    empleados["email"] = email
    empleados["sector"] = sector
    empleados["sueldo"] = sueldo
    return empleados

def mostrar_empleados(empleado: list)-> None:
    print("         ***Lista de empleados")
    print(" Legajo  Nombre Apellido Genero Edad Calle  Localidad  Provincia Email Sector Sueldo")
    print("-----------------------------------------------")
    for i in range(len(empleado)):
        mostrar_empleado(empleado[i])
    print()    

def mostrar_empleado(un_empleado: dict)-> None:
    print(f"{un_empleado["legajo"]} {un_empleado["nombre"] :>10} {un_empleado["apellido"] :>10} {un_empleado["genero"]} {un_empleado["edad"]} {un_empleado["calle"]} {un_empleado["localidad"]} {un_empleado["provincia"]} {un_empleado["email"]} {un_empleado["sector"]} {un_empleado["sueldo"]}") 

def buscar_empleado_por_legajo(lista: list, legajo: int)->int:
    indice = 0
    tam = len(lista)
    while indice < tam and legajo != lista[indice]["legajo"]:
        indice += 1
    if indice == tam:
        raise ValueError(f"No existe empleado con legajo {legajo}")
    else:
        return indice

def mapear_lista_nombre_sector(lista: list)->list:
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["nombre"], emp["sector"]))
    return lista_retorno

def mapear_campo_lista(lista:list, campo:str)-> list:
    lista_retorno = []
    for emp in lista:
        lista_retorno.append(emp[campo])
    return lista_retorno    

def mapear_lista(procesadora, lista:list)-> list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno  

def filtrar_empleados_sector(lista: list, sector:str)->list:
    lista_filtrada = []
    for emp in lista:
        if emp["sector"] == sector:
            lista_filtrada.append(emp)
    return lista_filtrada   

def filtrar_lista(filtradora, lista: list)->list:
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada

def mostrar_lista_tuplas(lista: list)->None:
    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento:15}", end="")
        print()

def for_each_lista(funcion, lista)->None:
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])

def reduce_lista(funcion, lista, valor_inicial = None):

    if valor_inicial != None:
        ant = valor_inicial
        indice = 0
    else:
        ant = lista[0]
        indice = 1

    for act in lista[indice:]:
        ant = funcion(ant, act)
    return ant

def ordenar_lista(comparator, lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if comparator(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista [j]
                lista[j] = aux


#empleado = {"nombre": "Juan", "apellido": "Perez", "edad": 20, "genero":"m", "Sector": "Info"} 

#filtrar_empleados_sector(empleado)