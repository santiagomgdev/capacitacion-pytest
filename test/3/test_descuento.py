from main import calcular_descuento

def test_descuento_10_por_ciento():
    assert calcular_descuento(1500) == 0.1

def test_descuento_5_por_ciento():
    assert calcular_descuento(800) == 0.05

def test_sin_descuento():
    assert calcular_descuento(300) == 0.0
