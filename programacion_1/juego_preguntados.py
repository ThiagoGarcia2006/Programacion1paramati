import random

# Diccionario de preguntas y respuestas
preguntas = {
    "¿Cuál es la capital de Francia?": "París",
    "¿Cuál es el río más largo del mundo?": "Amazonas",
    "¿En qué año comenzó la Segunda Guerra Mundial?": "1939",
    "¿Cuál es el planeta más grande del sistema solar?": "Júpiter",
    "¿Quién escribió 'El Quijote'?": "Miguel de Cervantes"
}

# Función para mostrar una pregunta aleatoria
def mostrar_pregunta():
    pregunta, respuesta = random.choice(list(preguntas.items()))
    print("Pregunta:", pregunta)
    return respuesta

# Función principal del juego
def jugar_preguntados():
    print("¡Bienvenido a Preguntados!")
    puntaje = 0
    while True:
        respuesta_correcta = mostrar_pregunta()
        respuesta_usuario = input("Tu respuesta: ").strip().capitalize()
        if respuesta_usuario == respuesta_correcta:
            puntaje += 1
            print("¡Respuesta correcta! Puntaje actual:", puntaje)
        else:
            print("Respuesta incorrecta. La respuesta correcta era:", respuesta_correcta)
            print("Tu puntaje final es:", puntaje)
            break

# Llamada a la función principal del juego
jugar_preguntados()
