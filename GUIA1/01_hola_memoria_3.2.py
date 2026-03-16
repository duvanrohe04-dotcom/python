
total_ahorrado = 0


for mes in range(1, 4):

   
    consignacion = int(input(f"¿Cuánto dinero vas a ahorrar en el mes {mes}?: "))

    
    total_ahorrado = total_ahorrado + consignacion


print(f"¡Ahorro completado! Tienes un total de: ${total_ahorrado}")