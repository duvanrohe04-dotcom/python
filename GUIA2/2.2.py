def convertir_moneda(cantidad: float, moneda: str = "COP") -> None:
    print(f"Procesando transacción: {cantidad} en moneda {moneda}")

convertir_moneda(5000, "USD")
convertir_moneda(15000)
