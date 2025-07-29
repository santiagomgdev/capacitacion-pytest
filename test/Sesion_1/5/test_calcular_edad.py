from main import calcular_edad

def test_calcular_edad():
    from datetime import date

    # Test cases
    assert calcular_edad(date(1981, 5, 4)) == 44 
    assert calcular_edad(date(2000, 2, 29)) == 25  # Año bisiesto
    assert calcular_edad(date(2001, 3, 1)) == 24
    assert calcular_edad(date(2025, 7, 1)) == 0

