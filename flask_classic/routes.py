from flask_classic import app
from flask import render_template, request, flash, redirect, session
from flask_classic.models import conexion_base, CambioMoneda, PageStatus
from flask_classic.config import APIKEY, SECRET_KEY
from flask_classic.conexion import *
from datetime import date, datetime, time


@app.route("/")
def index():
    dic_index = conexion_base()
    print(dic_index)
    no_data = False
    if not dic_index:
        no_data = True
        return render_template ("index.html", datos=dic_index, sin_data = no_data) 
    else:
        return render_template ("index.html", datos=dic_index)
        

def calcular_respuesta(request_form):
    q=0
    
    moneda_cambio = CambioMoneda([request_form['mfrom']])
    api_cambio = moneda_cambio.cambio(APIKEY, [request_form['mfrom'], request_form['mto']])   
    q = float(api_cambio) #esto seria la consulta a apicoin
    
    pu=float(request_form['qfrom'])/q
    respuesta = {
        'mfrom': request_form['mfrom'],
        'qfrom':request_form['qfrom'],
        'mto': request_form['mto'],
        'qto': q,
        'pu': pu
        }
    
    return respuesta

@app.route("/purchase", methods=['GET','POST'])
def compra():
    
    currency = [
        'EUR','BTC','ETH','USDT','BNB','XRP','ADA','SOL','DOT','MATIC'
        ] 
    
    if request.method == "GET":
        return render_template("forms.html", cur=currency)
    else:
        if request.form["btn"] == 'Calcular':
            respuesta = calcular_respuesta(request.form)
            return render_template('forms.html', cur=currency, request = respuesta)
            
        else:
            if request.form["btn"] == 'Guardar':
                respuesta = calcular_respuesta(request.form)
                reg_guardar = CambioMoneda(request.form['mfrom'])
                hora_actual=datetime.today().time().strftime('%H:%M:%S')
                registroForm = (None, date.today(), hora_actual, respuesta['mfrom'], respuesta['qfrom'], respuesta['mto'], respuesta['qto'])
                reg_guardar.registro(registroForm)
                
                return redirect("/")
            
    
            #flash ("Movimiento registrado")

           #aqui debe ir la funcion registro, que está dentro de la clase

            #hacer que inicio funcione en la pantalla de compra y estado tambien



@app.route("/status")
def estado():
    resultado_inversion=PageStatus.inversion()
    resultado_recuperado=PageStatus.recuperado()
    resultado_valor_compra= resultado_inversion[0][0] - resultado_recuperado [0][0]

    return render_template ("status.html", invertir=resultado_inversion[0][0], mon_recuperadas=resultado_recuperado[0][0], valor_compra = resultado_valor_compra)
