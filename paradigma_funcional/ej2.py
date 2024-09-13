

def fabrica_funciones(nombre):
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
    
    match nombre:
        case "s": return sumar
        case "r": return restar
        case "d": return dividir
        case "m": return multiplicar

a = 20
b = 10
miFuncion = fabrica_funciones("m")
print(miFuncion(a, b))



   