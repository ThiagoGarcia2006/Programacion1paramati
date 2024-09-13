def get_path_actual(nombre_archivo):
    import os 
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("personas.csv"), "r", encoding= "utf-8") as archivo:
    lista = []
    encabezado = archivo.readline().strip("\n").split(",")

    for linea in archivo.readlines():
        persona = {}
        linea = linea.strip("\n").split(",")


        id,nombre,apellido,genero,edad,peso = linea 
        persona["id"] = int(id)
        persona["nombre"] = nombre
        persona["apellido"] = apellido
        persona["edad"] = int(edad)
        persona["genero"] = genero
        persona["peso"] = float(peso)
        lista.append(persona)

for persona in lista:
    print(persona)

for i in range(len(lista)):
    lista[i]["nombre"] = lista[i]["nombre"].upper()


print("-----------------------------------------------------")

for persona in lista:
    print(persona)

with open(get_path_actual("personas_mayusculas.csv"), "w", encoding="utf-8") as archivo:
    encabezado = ",".join(list(lista[0].keys())) + "\n"
    archivo.write(encabezado)
    for persona in lista:
        values = list(persona.values())
        l = []
        for value in values:
            if isinstance(value, int):
                l.append(str(value))
            elif isinstance(value, float):
                l.append(str(value))
            else:
                l.append(value)
                
        linea = ",".join(l) + "\n"
        archivo.write(linea)


  
   
