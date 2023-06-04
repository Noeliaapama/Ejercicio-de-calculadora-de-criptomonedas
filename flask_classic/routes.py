from flask_classic import app
from flask import render_template, request, flash, redirect, session
from flask_classic.models import conexion_base, CambioMoneda, PageStatus
from flask_classic.config import APIKEY, SECRET_KEY
from flask_classic.conexion import *
from datetime import date, datetime, time

@app.route("/")
def index():
    dic_index = conexion_base()
    no_data = False
    disable_inicio = request.path == '/'
    if not dic_index:
        no_data = True
        return render_template ("index.html", datos=dic_index, sin_data = no_data, disable_ini=disable_inicio) 
    else:
        return render_template ("index.html", datos=dic_index, disable_ini=disable_inicio)
        

def calcular_respuesta(request_form):
    q=0
    moneda_cambio = CambioMoneda([request_form['mfrom']])
    api_cambio = moneda_cambio.cambio(APIKEY, [request_form['mfrom'], request_form['mto']])   
    q = float(api_cambio)
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
    disable_purchase = request.path == '/purchase'
    monedas_existentes = CambioMoneda.monedas_form()

    currency = [
        'EUR','BTC','ETH','USDT','BNB','XRP','ADA','SOL','DOT','MATIC'
        ] 

    if request.method == "GET":
        return render_template("forms.html", cur=currency, monexist=monedas_existentes, disable_purch=disable_purchase) 
    else:
        if request.form["btn"] == 'Calcular':
            respuesta = calcular_respuesta(request.form)

            return render_template('forms.html', cur=currency, request = respuesta, disable_purch=disable_purchase)

        else:
            if request.form["btn"] == 'Guardar':
                respuesta = calcular_respuesta(request.form)

                reg_guardar = CambioMoneda(request.form['mfrom'])
                sumas = CambioMoneda(request.form)
                sumas_qfrom = sumas.suma_qfrom(request.form['mfrom'])
                sumas_qto = sumas.suma_qto(request.form['mto'])
                resultado_suma = sumas_qfrom - sumas_qto
                if resultado_suma <= 0 and request.form['mfrom'] != 'EUR':                 
                    flash(f"No puedes vender más {request.form['mfrom']} de los que tienes actualmente")
                
                    return render_template('forms.html', cur=currency, request = respuesta, disable_purch=disable_purchase)
                else:
                    hora_actual=datetime.today().time().strftime('%H:%M:%S')
                    registroForm = (None, date.today(), hora_actual, respuesta['mfrom'], respuesta['qfrom'], respuesta['mto'], respuesta['qto'])
                    reg_guardar.registro(registroForm)

                return redirect("/")

@app.route("/status")
def estado():
    disable_status = request.path == '/status'
    resultado_inversion=PageStatus.inversion()
    resultado_recuperado=PageStatus.recuperado()
    if resultado_recuperado is None:
        resultado_recuperado = 0
    resultado_valor_compra=resultado_inversion - resultado_recuperado
    v_actual=PageStatus.valor_actual()

    return render_template ("status.html", invertir=resultado_inversion, mon_recuperadas=resultado_recuperado, valor_compra = resultado_valor_compra, val_actual=v_actual, disable_stat=disable_status)
