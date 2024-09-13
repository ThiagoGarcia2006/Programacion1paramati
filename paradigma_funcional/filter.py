def mapear_lista(procesadora, lista:list)-> list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno  

def filtrar_lista(filtradora, lista: list)->list:
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada

def for_each_lista(funcion, lista)->None:
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])

numeros = [4, 6, 5, 8, 7, 9]
print(sum(numeros))


numeros = [3, 2, 6, 5, 8, 3, 5]

# numeros impares multiplicados por 2

#lista = mapear_lista(lambda impar: impar * 2, filtrar_lista(lambda numero: numero % 2 != 0, numeros))

#resultado = filter(lambda n: n > 3, numeros)
resultado = list(map(lambda n: n * 2, numeros))

print(resultado)

for elemento in resultado:
    print(elemento)