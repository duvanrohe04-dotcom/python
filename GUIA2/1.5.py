def es_mayor_edad(edad: int) -> bool:
    if edad >= 18:
        return True
    else:
        return False

edad_usuario = int(input("Ingrese su edad: "))

if es_mayor_edad(edad_usuario):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
