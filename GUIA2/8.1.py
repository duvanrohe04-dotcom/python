class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            total = cantidad * self.precio
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre}")
            print(f"Total a pagar: ${total}")
            print(f"Stock restante: {self.stock}\n")

        except ValueError as e:
            print(f"Error al vender {self.nombre}: {e}\n")



class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento: int = dias_vencimiento



producto1 = Producto("Laptop", 2500, 5)
producto2 = ProductoPerecedero("Leche", 3.5, 10, 7)


producto1.vender(2)
producto2.vender(5)


producto1.vender(10)