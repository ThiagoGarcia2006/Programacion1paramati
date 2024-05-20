def mostrar_lista(lista:list) -> None:
    for indice in range(len(lista)):
        print(lista[indice], end= " ")


#pedir 5 numeros enteros al usuario y mostrarlo por consola

numeros = []
CANT = 5
nombres = ["Juan", "Ana", "Pedro", "Luisa"]

for i in range(CANT):
    numero = int(input("ingrese numero "))
    numeros.append(numero)

#for i in range(len(numeros)):
    #print(numeros[i], end=" ")
#print()   

mostrar_lista(numeros)




