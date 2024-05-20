


def calcular_superficie_circunferencia(radio = int)-> float:
    pi = 3.14
    return pi * radio ** 2

radio = int(input("Ingrese Radio "))

print(calcular_superficie_circunferencia(radio))

def calcular_superficie_rectangulo(base = int, altura = int)-> int:

    return base * altura

b = int(input("Ingrese Base "))
ah = int(input("Ingrese altura "))

print(calcular_superficie_rectangulo(b, ah))


