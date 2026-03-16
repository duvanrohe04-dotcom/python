

print("🧾 --- Caja Registradora ---")


total_compra = 0


for i in range(1, 6):
    precio = float(input(f"Ingrese el precio del producto {i}: $"))
    total_compra += precio   

print(f"\n💰 El costo total de la compra es: ${total_compra:.2f}")