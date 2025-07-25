import requests

def obtener_asociado_atlantis(identificacion: int):
    response = requests.get(f"https://api.atlantis.com/cooprodecol/asociados/{identificacion}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Asociado no encontrado")