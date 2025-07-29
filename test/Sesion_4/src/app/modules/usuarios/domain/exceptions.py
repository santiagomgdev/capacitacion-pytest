class DomainException(Exception):
    pass

class UsuarioExistenteException(DomainException):
    pass

class UsuarioNoEncontradoException(DomainException):
    pass