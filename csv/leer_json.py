import json

with open("./csv/personas.json", "r", encoding= "utf - 8") as archivo: 
    personas = json.load(archivo)

print(archivo.closed)


for persona in personas:
    print(persona)

print("---------------------------------------------------------")

for i in range(len(personas)):
    personas[i]["nombre"] = personas[i]["nombre"].upper()

with open("./csv/personas_nombre_mayuscula.json", "w", encoding= "utf -8") as archivo:
    json. dump(personas, archivo, indent=4)

