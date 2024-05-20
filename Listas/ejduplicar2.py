def duplicar(valores: int):

    for i in range(len(valores)):
        valores[i] = valores[i] * 2



lista = [3, 5, 6, 8, 3]
print(lista)

duplicar(lista)
print(lista)