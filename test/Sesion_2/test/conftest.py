import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import AsociadosAtlantis

@pytest.fixture
def db():
    base_datos = AsociadosAtlantis()
    yield base_datos
    base_datos.asociados.clear()