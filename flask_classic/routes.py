from flask_classic import app
from flask import render_template, request
from flask_classic.models import *
from flask_classic.config import APIKEY
from flask_classic.conexion import *


@app.route("/")
def index():
    dic_index = conexion()
    return render_template ("index.html", datos=dic_index) 
    
#rutas inicio, compra y estado 

@app.route("/purchase", methods=['GET','POST'])
def compra():
    currency = [
        'EUR','BTC','ETH','USDT','BNB','XRP','ADA','SOL','DOT','MATIC'
        ]    
    if request.method == "GET":
        return render_template("forms.html", cur=currency)
    else:
        if request.form["btn"] == 'Calcular':
            q = 0.756 #esto seria la consulta a apicoin
            pu=float(request.form['qfrom'])/q

            respuesta = {
                'from': q,
                'qfrom':request.form['qfrom'] ,
                'to': request.form['to'],
                'qto': request.form['qto'],
                'pu': str(pu)
            }
            return render_template('forms.html', cur=currency, request = respuesta)
        else:
            return "aqui se tiene que guardar en base de datos"




#hacer que inicio funcione en la pantalla de compra y estado tambien

@app.route("/status")
def estado():
    return render_template ("status.html")