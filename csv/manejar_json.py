import json

persona = {"id":10,"nombre":"Shalom","apellido":"Hallitt","genero":"Male","edad":24,"peso":76.9}

print(type(persona))
print(persona)

print("----------------------------------")

persona_json = json.dumps(persona)
print(type(persona_json))
print(persona_json)

print("------------------------------------")

persona2 = json.loads(persona_json)
print(type(persona2))
print(persona2)