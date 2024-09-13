#Agregar a funciones listas

def promedio_entero(a, b):
    return (a + b) // 2

def busqueda_binaria(lista: list, target:int)->int:
    inf = 0
    sup = len(lista) -1
    contador = 0
    while inf <= sup:
        medio = promedio_entero(inf, sup)
        contador += 1
        if lista [medio] == target:
            return medio
        elif target > lista [medio]:
            inf = medio + 1
        else:
            sup = medio -1
    raise ValueError(f"{target} is not in list")            
  

#lista= list(range(10000000000))

#lista = [4, 9, 11, 17, 21, 29, 34, 38, 41, 47, 56, 63, 71, 78, 89, 91, 103, 107, 120, 122]

#print(busqueda_binaria(lista, 17))

#empleado = {"nombre": "Juan", "apellido": "Perez", "edad": 20, "genero":"m"}

#print(empleado.items())

#print("-------------------------------")

#for key, value in empleado.items():
 #   print(key, value)

personas = [{"id":1,"nombre":"Franklyn","apellido":"Doers","genero":"Male","edad":44,"peso":119.8},
{"id":2,"nombre":"Carri","apellido":"Tommaseo","genero":"Female","edad":38,"peso":66.9},
{"id":3,"nombre":"Ewart","apellido":"Cowsby","genero":"Male","edad":64,"peso":76.8}]

lista = [3, 2, 5, 7, 1, 45, 32]

#def reduce_lista(funcion, lista, valor_inicial = None):

#    if valor_inicial != None:
#        ant = valor_inicial
#        indice = 0
#    else:
#        ant = lista[0]
#        indice = 1

#    for act in lista[indice:]:
#        ant = funcion(ant, act)
#    return ant
 
#resultado = reduce_lista(lambda ant, act : ant if ant < act["edad"] else act["edad"], personas, 100) 

#print(resultado)

def ordenar_lista(comparator, lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if comparator(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista [j]
                lista[j] = aux

ordenar_lista(lambda per1, per2: per1["peso"] < per2["peso"], personas)

for persona in personas:
    print(persona)

    
    
    




