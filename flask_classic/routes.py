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
    #ventas = CambioMoneda.venta(request_form['qfrom'], request_form['mfrom'])
    moneda_cambio = CambioMoneda([request_form['mfrom']])
    api_cambio = moneda_cambio.cambio(APIKEY, [request_form['mfrom'], request_form['mto']])   
    q = float(api_cambio) #esto seria la consulta a apicoin
    '''
    comparacion = ventas(request_form['mfrom'], request_form['qfrom'])
    if float(request_form['qfrom']) > comparacion:
        raise ValueError(f"No puedes vender {request_form['qfrom']} {request_form['mfrom']}: solo tienes {comparacion} disponible")
    '''
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
            #aqui va a ir el error de la funcion venta
            
            return render_template('forms.html', cur=currency, request = respuesta)
            
        else:
            if request.form["btn"] == 'Guardar':
                respuesta = calcular_respuesta(request.form)

                reg_guardar = CambioMoneda(request.form['mfrom'])
                # qfrom = reg_guardar.suma_qfrom(request.form['mfrom'])
                # qto = reg_guardar.suma_qto(request.form['mto'])
                # if qfrom - qto < 0:
                #     raise Exception("Error: qfrom - qto is negative")
                # try:
                #     sumas = CambioMoneda(cripto)
                #     sumas_qfrom = sumas.suma_qfrom(cripto)
                #     sumas_qto = sumas.suma_qto(cripto)
                #     resultado_suma = sumas_qfrom - sumas_qto
                #     resultado_suma > 0
                # except ValueError as error:
                #     flash("El no puedes vender más cantidad de la que tienes actualmente")

                hora_actual=datetime.today().time().strftime('%H:%M:%S')
                registroForm = (None, date.today(), hora_actual, respuesta['mfrom'], respuesta['qfrom'], respuesta['mto'], respuesta['qto'])
                reg_guardar.registro(registroForm)
                flash ("Movimiento registrado")

                return redirect("/")

            #hacer que inicio funcione en la pantalla de compra y estado tambien

@app.route("/status")
def estado():
    resultado_inversion=PageStatus.inversion()
    resultado_recuperado=PageStatus.recuperado()
    if resultado_recuperado[0][0] is None:
        resultado_recuperado = 0
    else:
        resultado_recuperado = resultado_recuperado[0][0]
    resultado_inversion = resultado_inversion[0][0]
    resultado_valor_compra=resultado_inversion - resultado_recuperado
    v_actual=PageStatus.valor_actual()

    return render_template ("status.html", invertir=resultado_inversion, mon_recuperadas=resultado_recuperado, valor_compra = resultado_valor_compra, val_actual=v_actual)
