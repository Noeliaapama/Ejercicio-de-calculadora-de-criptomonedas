import requests
from flask_classic.config import APIKEY
from flask_classic.routes import *
from flask_classic.conexion import *


class ModelError(Exception):
     pass

class CambioMoneda:
    def __init__(self):
        self.rate = None
        self.status_code= None
    def cambio(self, APIKEY, respuesta):
        mon1=respuesta[0]
        mon2=respuesta[2]
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{mon1}/{mon2}?{APIKEY}') #esta informacion viene de solicitudes HTTP
        li_currency =r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = li_currency ['rate']
            return li_currency['rate']
        else:
            raise ModelError(f"status: {r.status_code}, error: {li_currency['error']}")
        




