print("--- Filtro de Seguridad ---")

edades_acceso = [15, 22, 17, 30, 14]

for edad in edades_acceso:
   
    if edad >= 18:
        print(f"Persona de {edad} años: Acceso PERMITIDO.")
    else:
        print(f"Persona de {edad} años: Bloqueada.")