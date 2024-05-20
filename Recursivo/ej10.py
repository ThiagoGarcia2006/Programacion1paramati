
def pedir_entero_rango(l_inf: int, l_sup: int)->int:
    
    while True:
        try:
            numero = int(input(f"Ingrese un número entero entre {l_inf} y {l_sup}: "))
            if l_inf <= numero <= l_sup:
                return numero
            else:
                print("El número no está dentro del rango especificado. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")




edad = pedir_entero_rango(18, 65)

print(edad)