
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
numero = int(input("Ingresa un número del 1 al 7: "))
indice = numero - 1
if 0 <= indice < 7:
    print(f"El día correspondiente es: {dias_semana[indice]}")
else:
    print("Número inválido. Debe ser entre 1 y 7.")