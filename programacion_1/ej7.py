

def calcular_perimetro_circuntancial(radio: float)-> float:
    PI = 3.14
    perimetro = 2 * PI * radio
    return perimetro

radio = int(input("Radio "))

print(calcular_perimetro_circuntancial(radio))

#Otra manera podria ser con el import math

#perimetro = 2 * math.pi * radio

#Otra es con from math import pi

#perimetro = 2 * pi * radio ya que importa el pi de la caja math

def calcular_perimetro_rectangulo(base: int, altura: int)-> int:

    return 2 * (base + altura)

base = int(input("Base "))
altura = int(input("Altura "))


print(calcular_perimetro_rectangulo(base, altura))

def calcular_perimetro_cuadrado(lado: int)-> int:
    return 4 * lado

lado = int(input("Lados "))

print(calcular_perimetro_cuadrado(lado))
     
















