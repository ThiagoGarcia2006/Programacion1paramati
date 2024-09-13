from funciones_empleados import *
from data_empleados import *

#0 pedir un legajo y mostrar al empleado con ese legajo
legajo = 20009
try:
    indice = buscar_empleado_por_legajo(empleados, legajo)
    mostrar_empleado(empleados[indice])
except ValueError as ex:
    print(ex)
#1 mostrar por consola los nombres y sectores de los empleados

#mostrar_lista_tuplas(mapear_lista_nombre_sector(empleados))
mostrar_lista_tuplas(mapear_lista(lambda emp: (emp["nombres"], emp["sector"]), empleados))

#2 pedir un sector y mostrar los empleados de ese sector
sector = "Marketing"
#empleados_sector = filtrar_empleados_sector(empleados, sector)
empleados_sector = filtrar_lista(lambda emp : emp["sector"] == sector, empleados)
mostrar_empleados(empleados_sector)

#3 pedir un sector y mostrar el promedio de los sueldos de ese sector
sector = "Sistemas"
campo_promedio = "sueldo"
promedio_campo_sector( empleados, sector, campo_promedio)

print("-----------------------------------------------------")
#4 mostrar el promedio de sueldos de cada uno de los sectores
#5 mostrar el empleados que mas gana y a que sector pertenece
#6 mostrar el empleado o los empleados que tienen el mail mas corto y cuantos caracteres tiene
#7 decir cual es el sector que mas sueldo cobra
#8 decir cual es el sector que mas empleados tiene
#9 ordenar empleados por sector, dentro de un sector por genero y dentro del genero por legajo descendente

TAM = 10
empleados = []

cargar_lista_empleados_random(empleados, TAM)

mostrar_empleado(empleados)


