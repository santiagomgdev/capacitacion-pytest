import pytest

from src.main import AsociadosAtlantis

def test_obtener_estadisticas_todos_activos(db):
    db.add_asociado(1, "Ana", "ana@example.com", activo=True)
    db.add_asociado(2, "Luis", "luis@example.com", activo=True)
    db.add_asociado(3, "Marta", "marta@example.com", activo=True)

    resultado = db.obtener_estadisticas()

    assert resultado["total_asociados"] == 3
    assert resultado["asociados_activos"] == 3


def test_obtener_estadisticas_activos_e_inactivos(db):
    db.add_asociado(1, "Ana", "ana@example.com", activo=True)
    db.add_asociado(2, "Luis", "luis@example.com", activo=False)
    db.add_asociado(3, "Marta", "marta@example.com", activo=True)

    resultado = db.obtener_estadisticas()

    assert resultado["total_asociados"] == 3
    assert resultado["asociados_activos"] == 2


def test_obtener_estadisticas_todos_inactivos(db):
    db.add_asociado(1, "Pedro", "pedro@example.com", activo=False)
    db.add_asociado(2, "Laura", "laura@example.com", activo=False)

    resultado = db.obtener_estadisticas()

    assert resultado["total_asociados"] == 2
    assert resultado["asociados_activos"] == 0


def test_obtener_estadisticas_sin_asociados(db):
    resultado = db.obtener_estadisticas()

    assert resultado["total_asociados"] == 0
    assert resultado["asociados_activos"] == 0
