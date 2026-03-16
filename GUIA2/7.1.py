class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 10000

    def solicitar_retiro(self) -> None:
        print("--- Bienvenido al cajero ---")

        try:
            monto_str: str = input("Ingrese la cantidad a retirar: ")
            monto: float = float(monto_str)

            if monto == 0:
                raise ValueError("No puedes retirar cero pesos")

            if monto > self.efectivo_disponible:
                print("No hay suficiente dinero en el cajero")
            else:
                self.efectivo_disponible -= monto
                print(f"Retiro exitoso. Quedan ${self.efectivo_disponible} en el cajero")

        except ValueError:
            print("Error de formato: usted ingresó caracteres inválidos")

        finally:
            print("Expulsando tarjeta... Gracias por utilizar nuestra red.\n")



mi_cajero = CajeroAutomatico()


mi_cajero.solicitar_retiro()