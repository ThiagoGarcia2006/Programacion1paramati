#from time import sleep
from matematicas import *

def saludar():
    print("Hola")

def despedir():
    print("Chau")

def ejecutora(x):
    x()



#saludar()
#despedir()

#ejecutora(saludar)
#ejecutora(despedir)

#x = saludar

#x()

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def multiplicar(a, b):
    return a * b

def operar(operacion, op1, op2):
    sleep(3)
    return operacion(op1, op2)


print(operar(sumar, 4, 5))
print(operar(restar, 4, 5))
print(operar(multiplicar, 4, 5))
print(operar(dividir, 4, 5))



