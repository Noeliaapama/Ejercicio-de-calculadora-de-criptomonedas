from flask_classic import app
from flask import render_template
from flask_classic.models import *

@app.route("/")
def index():
    dic_index = conexion()

    return render_template ("index.html", datos=dic_index) 
    
#rutas inicio, compra y estado 

@app.route("/purchase")
def compra():
    return render_template ("forms.html")

#hacer que inicio funcione en la pantalla de compra y estado tambien

@app.route("/status")
def estado():
    return render_template ("status.html")