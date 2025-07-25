import pytest
from main import dividir

def test_division_normal():
    assert dividir(10, 2) == 5

def test_division_negativos():
    assert dividir(-10, 2) == -5

def test_division_decimal():
    assert dividir(7, 2) == 3.5

def test_division_por_uno():
    assert dividir(7, 1) == 7

def test_division_por_si_mismo():
    assert dividir(7, 7) == 1

def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por 0"):
        dividir(10, 0)