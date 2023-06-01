import requests
from flask_classic.config import APIKEY
from flask_classic.routes import *
from flask_classic.conexion import *
from flask_classic import BBDD

def conexion_base(): #aqui hacemos la conexion con la base de datos
    conectar = Conexion ("SELECT * FROM mov_criptos;")
    fila = conectar.res.fetchall() 
    columna = conectar.res.description
    #necesitamos crearnos un diccionario de rutas index
    li_diccionario=[]
    if fila:
        for f in fila:
            diccionario = {}
            posicion = 0
            for c in columna:
                diccionario[c[0]] = f[posicion]
                posicion += 1
            li_diccionario.append(diccionario)
    conectar.con.close() #cerramos la query
    return li_diccionario

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
        mon2 = respuesta[1]

        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{mon1}/{mon2}?apikey={APIKEY}') #esta informacion viene de solicitudes HTTP
        li_currency =r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = li_currency ['rate']
            rate= self.rate
            return rate
        else:
            raise ModelError(f"status: {r.status_code}, error: {li_currency['error']}")
        
        
    def registro(self, registroForm):
        conect_registro = Conexion(f"INSERT INTO mov_criptos ('id', 'date', 'time', 'mfrom', 'quantity_from', 'mto', 'quantity_to') VALUES (?,?,?,?,?,?,?)", registroForm)
        conect_registro.con.commit()
        conect_registro.con.close()
    

class PageStatus:

    def __init__(self):
        pass

    def inversion():
        conect_inv = Conexion(f"SELECT SUM (quantity_from) FROM mov_criptos WHERE quantity_from > 0")
        result_inv = conect_inv.res.fetchall()
        conect_inv.con.close()
        return result_inv

    def recuperado():       
        conect_recup = Conexion(f"SELECT SUM(quantity_to) FROM mov_criptos WHERE mto = 'EUR' AND quantity_from > 0")
        result_recup = conect_recup.res.fetchall()
        conect_recup.con.close()
        return result_recup
    
    def valor_actual():
        conect_valor = Conexion("SELECT DISTINCT mto FROM mov_criptos")
        query = conect_valor.res

        moneda_cripto = [fila[0] for fila in query.fetchall()]

        valor_total = 0

        for cripto in moneda_cripto:
            conect_cantidad = Conexion(f"SELECT SUM(quantity_to) - SUM(quantity_from) FROM mov_criptos WHERE mto = '{cripto}' OR mfrom = '{cripto}'")
            cantidad = conect_cantidad.res.fetchone()[0]
            respuesta_valor = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{cripto}/EUR?apikey={APIKEY}")
            cambio_valor = respuesta_valor.json()["rate"]

            valor = cantidad * cambio_valor
            valor_total += valor

        return valor_total




        

        




