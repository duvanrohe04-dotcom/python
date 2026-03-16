print("--- Diagnóstico de red ---")

hay_internet = input("¿El módem tiene luces encendidas? (si/no): ")

if hay_internet == "si":
    luz_roja = input("¿Alguna de las luces es color ROJO? (si/no): ")
    
    if luz_roja == "si":
        print("Fallo detectado: Problema en la fibra óptica. Llame a soporte.")
    else:
        print("Todo normal: Su conexión está operando al 100%.")
else:
    print("Fallo crítico: Verifique que el equipo esté conectado a la corriente.")
