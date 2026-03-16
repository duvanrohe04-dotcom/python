def crear_perfil(nombre: str , rol : str )-> None:
    print(f"Registarndo una base de datos{nombre} | permisos: {rol}")
    crear_perfil("Carlos", "Admin")
    crear_perfil("Ana", "ventas")