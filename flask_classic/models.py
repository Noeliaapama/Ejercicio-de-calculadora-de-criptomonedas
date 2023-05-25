import requests
import sqlite3
from flask_classic.config import APIKEY
from flask_classic.routes import *




def conexion(): #aqui hacemos la conexion con la base de datos
    con = sqlite3.connect("data/mov_criptos.sqlite")
    cur = con.cursor()
    res = cur.execute ("select * from mov_criptos;")
    #necesitamos recorrer la información de la base de datos
    fila = res.fetchall() 
    columna = res.description
    #necesitamos crearnos un diccionario de rutas index
    li_diccionario=[]

    for f in fila:
        diccionario = {}
        posicion = 0
        for c in columna:
            diccionario[c[0]] = f[posicion]
            posicion += 1
    li_diccionario.append(diccionario)
    con.close() #cerramos la query
    return li_diccionario

class ModelError(Exception):
     pass

class CambioMoneda:
    def __init__(self):
        self.rate = None
        self.status_code= None
    def cambio(self, APIKEY, currency):
        cripto = currency       
        r = requests.get(f'https://rest.coinapi.io/{cripto}/{cripto}?{APIKEY}') #esta informacion viene de solicitudes HTTP
        li_currency =r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = li_currency ['rate']
        else:
            raise ModelError(f"status: {r.status_code}, error: {li_currency['error']}")
        
        return 



