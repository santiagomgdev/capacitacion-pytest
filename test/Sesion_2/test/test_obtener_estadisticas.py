import pytest

from src.main import AsociadosAtlantis

def test_obtener_estadisticas():
    asociado = AsociadosAtlantis()
    asociado.add_asociado(1, "Ana", "ana@example.com", activo=True)
    asociado.add_asociado(2, "Luis", "luis@example.com", activo=False)
    asociado.add_asociado(3, "Marta", "marta@example.com", activo=True)

    resultado = asociado.obtener_estadisticas()

    assert resultado["total_asociados"] == 3
    assert resultado["asociados_activos"] == 2