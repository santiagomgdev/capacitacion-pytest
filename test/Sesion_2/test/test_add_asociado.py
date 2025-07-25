import pytest

def test_add_asociado_exitoso(db):
    #arr
    asociadoid:int=1
    nombre:str="prueba"
    correo:str="prueba@example.com"
    #act
    res=db.add_asociado(asociado_id=asociadoid,nombre=nombre,correo=correo)
    #assert
    assert res==True

def test_add_asociado_duplicado(db):
    #arr
    asociadoid:int=1
    nombre:str="prueba"
    correo:str="prueba@example.com"
    #act
    re1=db.add_asociado(asociado_id=asociadoid,nombre=nombre,correo=correo)
    with pytest.raises(ValueError,match="Asociado ya existe"):
        res2=db.add_asociado(asociado_id=asociadoid,nombre=nombre,correo=correo)

def test_add_asociado_email_duplicado(db):
    #arr
    asociadoid1:int=1
    nombre1:str="prueba"
    correo1:str="prueba@example.com"
    asociadoid2:int=2
    nombre2:str="test"
    correo2:str="prueba@example.com"
    #act
    re1=db.add_asociado(asociado_id=asociadoid1,nombre=nombre1,correo=correo1)
    with pytest.raises(ValueError,match="Asociado con correo duplicado"):
        res2=db.add_asociado(asociado_id=asociadoid2,nombre=nombre2,correo=correo2)