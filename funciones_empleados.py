

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

def filtrar_empleados_sector(lista: list, sector:str)->list:
    empleados_filtrados = []
    for nombre, sec in lista:
        if sec == sector:
            empleados_filtrados.append((nombre, sec))
    return empleados_filtrados   

def mostrar_lista_tuplas(lista: list)->None:
    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento:15}", end="")
        print()


empleado = {"nombre": "Juan", "apellido": "Perez", "edad": 20, "genero":"m", "Sector": "Info"} 

filtrar_empleados_sector(empleado)
