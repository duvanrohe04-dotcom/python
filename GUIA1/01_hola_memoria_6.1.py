
estudiantes = [
    {"nombre": "Ana", "nota": 90},
    {"nombre": "Luis", "nota": 50}
]

for persona in estudiantes:
    if persona["nota"] >= 60:
        print(f"{persona['nombre']} ha APROBADO con {persona['nota']}")
    else:
        print(f"{persona['nombre']} ha REPROBADO con {persona['nota']}")