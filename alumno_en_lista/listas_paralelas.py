from funciones_paralelas import *
from data_warehouse import *

#for x in alumnos:   
    #mostrar_alumno(x[0], x[1], x[2], x[3], x[4], x[5])

TAM = 3
alumnos = []

legajos = []
nombres = []
generos = []
notas_p1 = []
notas_p2 = []
promedios = []

for _ in range(TAM):
    aux = int(input("Ingrese legajo: "))
    legajos.append(aux)
    aux = input("Ingrese nombre: ")
    nombres.append(aux)
    aux = input("Ingrese genero: ")
    generos.append(aux)
    aux = int(input("Ingrese nota primer parcial: "))
    notas_p1.append(aux)
    int(input("Ingrese nota segundo parcial: "))
    notas_p2.append(aux)
    promedio = calcular_promedio(notas_p1[-1], notas_p2[-1])
    promedios.append(promedio) 


#cargar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios, TAM)

#mostrar_alumno(legajos, nombres, generos, notas_p1, notas_p2, promedios)

#ordenar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)

#mostrar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)

