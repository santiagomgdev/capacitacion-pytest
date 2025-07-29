import pytest

from src.main import obtener_asociado_atlantis

def test_obtener_asociado(mocker):

    # Mockear petición 
    mock_peticion = mocker.patch("src.main.requests.get")

    # Establecer valores de respuesta

    mock_peticion.return_value.status_code = 200
    mock_peticion.return_value.json.return_value = {
        "nombre": "Pablo",
        "identificacion": 21323412,
        "correo": "example@coop.com"
    }

    # Act

    result = obtener_asociado_atlantis(21323412)

    # Asserts

    assert result == {
        "nombre": "Pablo",
        "identificacion": 21323412,
        "correo": "example@coop.com"
    }
    mock_peticion.assert_called_once_with("https://api.atlantis.com/cooprodecol/asociados/21323412")