from flask_classic import app
from flask import render_template, request, flash, redirect, session
from flask_classic.models import conexion_base, CambioMoneda
from flask_classic.config import APIKEY, SECRET_KEY
from flask_classic.conexion import *
from datetime import date, datetime, time


@app.route("/")
def index():
    dic_index = conexion_base()
    no_data = False
    if not dic_index:
        no_data = True
        return render_template ("index.html", datos=dic_index, sin_data = no_data) 
    else:
        return render_template ("index.html", datos=dic_index) 


def calcular_respuesta(request_form):
    q=0.123
    '''
    moneda_cambio = CambioMoneda([request_form['from']])
    api_cambio = moneda_cambio.cambio(APIKEY, [request_form['from'], request_form['to']])   
    q = float(api_cambio) #esto seria la consulta a apicoin
    '''
    pu=float(request_form['qfrom'])/q
    respuesta = {
        'from': request_form['from'],
        'qfrom':request_form['qfrom'],
        'to': request_form['to'],
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
            '''
            moneda_cambio = CambioMoneda([request.form['from']])
            api_cambio = moneda_cambio.cambio(APIKEY, [request.form['from'], request.form['to']])   
            q = float(api_cambio) #esto seria la consulta a apicoin
            pu=float(request.form['qfrom'])/q

            respuesta = calculate_response(request.form)
            return render_template('forms.html', cur=currency, request=respuesta)
            
            respuesta = {
                'from': request.form['from'],
                'qfrom':request.form['qfrom'],
                'to': request.form['to'],
                'qto': q,
                'pu': pu
                }
            '''
            
            # Se guarda la respuesta del formulario en la sesión de flask
            # form_data = request.form.to_dict()
            # session['form_data'] = form_data
            
            # return render_template('forms.html', cur=currency, request = respuesta,form_data=form_data)

            return render_template('forms.html', cur=currency, request = respuesta)
            
        else:
            if request.form["btn"] == 'Guardar':
                respuesta = calcular_respuesta(request.form)
    
                '''
                moneda_cambio = CambioMoneda([request.form['from']])
                api_cambio = moneda_cambio.cambio(APIKEY, [request.form['from'], request.form['to']])   
                q = float(api_cambio) #esto seria la consulta a apicoin
                pu=float(request.form['qfrom'])/q

                respuesta = {
                    'from': request.form['from'],
                    'qfrom':request.form['qfrom'],
                    'to': request.form['to'],
                    'qto': q,
                    'pu': pu
                    }
                '''
            
                reg_guardar = CambioMoneda(request.form['from'])
                registroForm = (None, date.today(), datetime.today(), respuesta['from'], respuesta['qfrom'], respuesta['to'], respuesta['qto'])
                                #request.form['from'], request.form['qfrom'], request.form['to'], q) 
                reg_guardar.registro(registroForm)
                return redirect("/")
            #flash ("Movimiento registrado")

           #aqui debe ir la funcion registro, que está dentro de la clase

            #hacer que inicio funcione en la pantalla de compra y estado tambien

@app.route("/status")
def estado():
    return render_template ("status.html")