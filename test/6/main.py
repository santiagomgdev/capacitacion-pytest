def dividir(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("No se puede dividir por 0")
    return a / b