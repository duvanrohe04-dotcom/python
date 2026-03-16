colores = ["Rojo", "Azul", "Verde"]

print(f"Lista inicial: {colores}")

color_eliminar = input("Escribe un color que no te guste: ")


if color_eliminar in colores:
    colores.remove(color_eliminar)
    print("Color eliminado correctamente.")
else:
    print("Ese color no está en la lista.")

print(f"Lista final: {colores}")
