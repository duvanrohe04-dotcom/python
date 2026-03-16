print("=== Control de acceso a la montaña rusa ===")

altura = float(input("Ingrese su altura en cm: "))
edad = int(input("Ingrese su edad: "))

if altura > 150 and edad > 12:
    print("Acceso permitido")
else:
    print("Acceso denegado")