import pytest
from src.main import AsociadosAtlantis

@pytest.fixture
def db():
    base_datos = AsociadosAtlantis()
    yield base_datos
    base_datos.asociados.clear()