from main import formatear_nombre_cliente

def test_formatear_nombre_cliente_correcta():
    #arr
    nombre:str="duber   "
    apellido:str="garcia"
    #act
    res=formatear_nombre_cliente(nombre,apellido)
    #asserts
    assert isinstance(res,str)
    assert res == "GARCIA, Duber"
    

def test_formatear_nombre_cliente_sin_nombre():
    #arr
    nombre:str=""
    apellido:str="garcia"
    #act
    res=formatear_nombre_cliente(nombre,apellido)
    #asserts
    assert isinstance(res,str)
    assert res == ""


def test_formatear_nombre_cliente_sin_apellido():
    #arr
    nombre:str="duber"
    apellido=None
    #act
    res=formatear_nombre_cliente(nombre,apellido)
    #asserts
    assert isinstance(res,str)
    assert res == "DUBER"