# Código en Python3 para calcular la edad en años
from datetime import date

def calcular_edad(nacimiento: date):
    hoy = date.today()
    try: 
        fecha = nacimiento.replace(year = hoy.year)

    # Se lanza cuando la fecha de nacimiento es 29 de febrero
    # y el año actual no es bisiesto
    except ValueError: 
        fecha = nacimiento.replace(year = hoy.year,
                  month = nacimiento.month + 1, day = 1)

    if fecha > hoy:
        return hoy.year - nacimiento.year - 1
    else:
        return hoy.year - nacimiento.year
