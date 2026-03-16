def calcular_iva(precio_base: float)-> float:
    iva: float = precio_base * 0.19
    precio_final: float = precio_base + iva
    return precio_final

factura_1: float = calcular_iva(1000)
factura_2: float = calcular_iva(5000)
   
print(factura_1, factura_2)
   