concesionario = []

# Bucle que se repite 3 veces
for i in range(3):
    print(f"\nRegistro del vehículo #{i + 1}")

    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    precio = input("Ingrese el precio del vehículo: ")

    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }

    concesionario.append(vehiculo)

print("\n=== INFORME DEL CONCESIONARIO ====")

for carro in concesionario:
    print(f"Vehículo registrado: Marca {carro['marca']}, "
          f"Modelo {carro['modelo']}, "
          f"Precio: ${carro['precio']}")

print("==================================")