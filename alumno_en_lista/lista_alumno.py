from funciones_alumnos_lista import *



#alumnos = [
#    [2000, "Juan", "m", 6, 7, 6.50]
#    [2001, "Juana", "f", 6, 7, 6.50]
#    [2002, "Maria", "f", 6, 7, 6.50]
#    [2003, "Luis", "m", 6, 7, 6.50]
#    [2004, "Sofia", "f", 6, 7, 6.50]   
#]

#for x in alumnos:   
#    mostrar_alumno(x[0], x[1], x[2], x[3], x[4], x[5])

TAM = 4
alumnos = []

for _ in range(TAM):
    nuevo_alumno = []
    aux = int(input("Ingrese legajo: "))
    nuevo_alumno.append(aux)
    aux = input("Ingrese nombre: ")
    nuevo_alumno.append(aux)
    aux = input("Ingrese genero: ")
    nuevo_alumno.append(aux)
    aux = int(input("Ingrese nota primer parcial: "))
    nuevo_alumno.append(aux)
    int(input("Ingrese nota segundo parcial: "))
    nuevo_alumno.append(aux)
    promedio = calcular_promedio(nuevo_alumno[3], nuevo_alumno[4])
    nuevo_alumno.append(promedio)
    alumnos.append(nuevo_alumno)

mostrar_alumnos(alumnos)  
cargar_alumnos(alumnos, TAM)
ordenar_alumnos(alumnos)
