edad_usuario = int(input("Por favor, ingresa tu edad en números: "))
print("Evaluando procesos de acceso...")

if edad_usuario >= 18:
    print("Acceso concedido: eres mayor de edad")
elif edad_usuario >= 13:
    print("Acceso restringido: eres adolescente")
else:
    print("Acceso denegado: eres menor de edad")
print("gracias por usar el sistema")



