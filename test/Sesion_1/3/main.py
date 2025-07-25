def calcular_descuento(compras_totales: int) -> float:
    if compras_totales > 1000: return 0.1
    elif compras_totales > 500: return 0.05
    return 0.0