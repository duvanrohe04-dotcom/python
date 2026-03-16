class MascotaVirtual:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.energia: int = 10

    def jugar(self) -> None:
        self.energia -= 3
        print(f"{self.nombre} jugó. Energía actual: {self.energia}")

    def dormir(self) -> None:
        self.energia += 5
        print(f"{self.nombre} durmió. Energía actual: {self.energia}")



mascota = MascotaVirtual("pulgoso")

mascota.jugar()
mascota.dormir()