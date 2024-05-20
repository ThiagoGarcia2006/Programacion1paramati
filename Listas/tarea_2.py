# tarea pedir 10 numeros usando una lista y calcular la sumatoria, el promedio, el mayor y cuantas veces esta repetido

# Pedir 10 números
numeros = []
for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

# Calcular la sumatoria
sumatoria = sum(numeros)

# Calcular el promedio
promedio = sumatoria / len(numeros)

# Encontrar el número mayor
mayor = max(numeros)

# Contar cuántas veces está repetido el número mayor
repeticiones_mayor = numeros.count(mayor)

print("Sumatoria:", sumatoria)
print("Promedio:", promedio)
print("Mayor:", mayor)
print("El número mayor está repetido", repeticiones_mayor, "veces.")
