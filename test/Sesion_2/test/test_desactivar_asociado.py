import pytest
from src.main import AsociadosAtlantis  


class TestDesactivarAsociado:
    
    def setup_method(self):
        """Setup inicial para cada test"""
        self.atlantis = AsociadosAtlantis()
        
        
        
        # CP-001 
        
    def test_desactivar_asociado_existente_activo(self):
        """
        Caso 1: Desactivar un asociado que existe y está activo
        Resultado esperado: True, y el asociado debe quedar inactivo
        """
        # Arrange
        self.atlantis.add_asociado(1, "Juan Pérez", "juan@email.com", True)
        
        # Act
        resultado = self.atlantis.desactivar_asociado(1)
        
        # Assert
        assert resultado == True
        asociado = self.atlantis.get_asociado_by_id(1)
        assert asociado["activo"] == False
        
        
        
        
        # CP-0002  
        
        
    def test_desactivar_asociado_existente_ya_inactivo(self):
        """
        Caso 2: Desactivar un asociado que existe pero ya está inactivo
        Resultado esperado: True, y el asociado debe seguir inactivo
        """
        # Arrange
        self.atlantis.add_asociado(2, "María García", "maria@email.com", False)
        
        # Act
        resultado = self.atlantis.desactivar_asociado(2)
        
        # Assert
        assert resultado == True
        asociado = self.atlantis.get_asociado_by_id(2)
        assert asociado["activo"] == False
        
        
        
        # CP-003 
        
    def test_desactivar_asociado_inexistente(self):
        """
        Caso 3: Intentar desactivar un asociado que no existe
        Resultado esperado: False
        """
        # Act
        resultado = self.atlantis.desactivar_asociado(999)
        
        # Assert
        assert resultado == False
        
        
        
        
        # CP-004 
        

        
    def test_desactivar_asociado_con_id_none(self):
        """
        Caso 4: Intentar desactivar con ID None
        Resultado esperado: False (manejo de valor None)
        """
        # Act
        resultado = self.atlantis.desactivar_asociado(None)
        
        # Assert
        assert resultado == False
        
        
        
        
        # CP-005 
        
        
        
    def test_desactivar_asociado_verificar_otros_no_afectados(self):
        """
        Caso 5: Desactivar un asociado y verificar que otros no se vean afectados
        Resultado esperado: Solo el asociado específico debe ser desactivado
        """
        # Arrange
        self.atlantis.add_asociado(1, "Juan Pérez", "juan@email.com", True)
        self.atlantis.add_asociado(2, "María García", "maria@email.com", True)
        self.atlantis.add_asociado(3, "Pedro López", "pedro@email.com", False)
        
        # Act
        resultado = self.atlantis.desactivar_asociado(1)
        
        # Assert
        assert resultado == True
        
        # Verificar que solo el asociado 1 fue desactivado
        assert self.atlantis.get_asociado_by_id(1)["activo"] == False
        assert self.atlantis.get_asociado_by_id(2)["activo"] == True  # No debe cambiar
        assert self.atlantis.get_asociado_by_id(3)["activo"] == False  # Ya estaba inactivo
        
        # Verificar estadísticas
        stats = self.atlantis.obtener_estadisticas()
        assert stats["total_asociados"] == 3
        assert stats["asociados_activos"] == 1  # Solo María debe estar activa