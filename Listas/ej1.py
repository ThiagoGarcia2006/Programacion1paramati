

"""
#l1 = list()
l2 = []

print(id(l2))

#print(l1)
#print(l2)
#print(type(l1))
#print(type(l2))

l2.append(5)
print(l2)

l2.append(14)
print(l2)

l2.append(57)
print(l2)
"""

lista = [34, 65, 12, 87, 42, 90, 31, 54, 18, 44, 77]

mayor = max(lista) #mayor
menor = min(lista) #menor
lista.insert(3, 44) #inserta
print(lista.count(44)) #cantidad de tal numero
lista.remove(65) #sacar numero
lista.sort()   #Mayor a menor


print(mayor)
print(menor)
print(lista)

"""
#de tal numero a tal numero
print(lista[3:]) 
print(lista[:5])
"""


#print(lista[len(lista)-1])
#print(lista[-1])