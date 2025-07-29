import pytest
from main import Database

@pytest.fixture
def db():
    base_datos = Database()
    yield base_datos
    base_datos.asociados.clear() # Cleanup

def test_creacion_asociado(db):
    db.add_asociado(1, "Pedro", "correo@example.com")
    assert db.get_asociado_by_id(1)["nombre_asociado"] == "Pedro"

def test_creacion_usuario_duplicado(db):
    db.add_asociado(1, "Pedro", "pedro@example.com")
    with pytest.raises(ValueError, match="Usuario ya existe"):
        db.add_asociado(1, "Pablo", "pablo@example.com")