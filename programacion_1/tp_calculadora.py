


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def multiplicar(a, b):
    return a * b



numero1 = int(input("Ingrese un numero: "))

numero2 = int(input("Ingrese otro numero: "))

operacion = input("Ingrese la operación (suma, resta, dividir, multiplicar): ").lower()

if operacion == 'suma':
    resultado = suma(numero1, numero2)
elif operacion == 'resta':
    resultado = resta(numero1, numero2)
elif operacion == 'dividir':
    resultado = dividir(numero1, numero2)
elif operacion == 'multiplicar':
    resultado = multiplicar(numero1, numero2)
else:
    resultado = "Operación no válida."


print("El resultado es:", resultado)

print("Hasta luego!! ")



            

