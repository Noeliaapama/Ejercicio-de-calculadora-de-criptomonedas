import requests
from flask_classic.config import APIKEY
from flask_classic.routes import *
from flask_classic.conexion import *


class ModelError(Exception):
     pass

class CambioMoneda:
    def __init__(self, cripto):
        self.li_criptos=[]
        self.li_no_criptos=[]
        self.mon_cripto= cripto
        self.rate = None
        self.status_code= None
        self.time = None

    def todas_las_monedas(self,APIKEY):
        r = requests.get(f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}")
        if r.status_code != 200:
            raise Exception("Error en consulta: {}".format(r.status_code))
        
        li_currency = r.json()
    
        for item in li_currency:

            if item ["type_is_crypto"] == 1:
                self.li_criptos.append(item["asset_id"])
            else:
                self.li_no_criptos.append(item["asset_id"])

    def cambio(self, APIKEY, respuesta):
        mon1 = respuesta[0]
        mon2 = respuesta[2]

        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{mon1}/{mon2}?apikey={APIKEY}') #esta informacion viene de solicitudes HTTP
        li_currency =r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = li_currency ['rate']
            self.time = li_currency ['time']
        else:
            raise ModelError(f"status: {r.status_code}, error: {li_currency['error']}")
        
    def registro(registroForm):
        con = sqlite3.connect ("data/mov_criptos.sqlite")
        cur = con.cursor()
        res = cur.execute("insert into mov_criptos (id, date, time, from, quantity_from, to, quantity_to) values (?,?,?)", registroForm)

        con.commit()
        con.close


class PageStatus:
    def inversion():
        conect_inv = conexion("select sum (quantity_from) from mov_criptos where quantity > 0")
        result_inv = conect_inv.res.fetchall()
        conect_inv.con.close()
        return result_inv
    #comprobar después si funciona, ya que es una base pero no está comprobado

    def recuperado():
        conect_recup = conexion("select sum (quantity_to) from mov_criptos where quantity > 0")
        result_recup = conect_recup.res.fetchall()
        conect_recup.con.close()
        return result_recup
    
    def valor_total():
        conect_vato= conexion("select quantity_from-quantity_to as resultado from mov_criptos")
        resultado = conect_vato.res.fectchall()
        conect_vato.con.close()
        return resultado
    
    #falta valor actual



        

        




