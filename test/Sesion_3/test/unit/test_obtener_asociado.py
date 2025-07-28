import pytest
from src.interface.asociado import AsociadoInterface
from src.models.asociado import Asociado
from src.repository.asociado import obtener_asociado

def test_obtener_asociado(mocker):
    # Arrange
    mock_create_engine = mocker.patch('src.repository.asociado.create_engine')
    mock_session_class = mocker.patch('src.repository.asociado.Session')
    expected_asociado = Asociado(id=1, nombre="Juan", edad=25)
    
    mock_session_class.return_value.execute.return_value.scalar.return_value = expected_asociado
    
    # Act
    result = obtener_asociado("Juan")
    
    # Assert
    mock_create_engine.assert_called_once_with(
        "mysql+pymysql://usuario:hola123@172.20.1.20:3306/bdatlantissico", 
        echo=True
    )
    mock_session_class.assert_called_once_with(mock_create_engine.return_value)
    mock_session_class.return_value.execute.assert_called_once()
    mock_session_class.return_value.execute.return_value.scalar.assert_called_once()
    assert result == AsociadoInterface.from_model(expected_asociado)
