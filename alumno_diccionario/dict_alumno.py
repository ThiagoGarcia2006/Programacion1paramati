from funciones_dicc import *
from data_warehouse import *


    
"""
alumnos = [
    [2000, "Juan", "m", 6, 7, 6.50]
    [2001, "Juana", "f", 6, 7, 6.50]
    [2002, "Maria", "f", 6, 7, 6.50]
    [2003, "Luis", "m", 6, 7, 6.50]
    [2004, "Sofia", "f", 6, 7, 6.50]   
]

for x in alumnos:   
    mostrar_alumno(x[0], x[1], x[2], x[3], x[4], x[5])
"""

TAM = 5
alumnos = []

"""
for _ in range(TAM):
    nuevo_alumno = {}
    legajo = int(input("Ingrese legajo: "))
    
    nombre = input("Ingrese nombre: ")
    
    genero = input("Ingrese genero: ")
   
    notap1 = int(input("Ingrese nota primer parcial: "))
    
    notap2 = int(input("Ingrese nota segundo parcial: "))
    
    alumnos.append(new_alumno(legajo, nombre, genero, notap1, notap2))
"""

mostrar_alumnos(alumnos)  
cargar_alumnos(alumnos, TAM)
ordenar_alumnos(alumnos)