from flask_classic import app
from flask import render_template
from flask_classic.models import *

@app.route("/")
def index():
    datos_prueba = [
        {'id':1,'date':'2023-05-14', 'time':'10:00', 'from': 'ETH', 'quantity_from': 123, 'To': '€', 'quantity_to': 123 },
        {'id':2,'date':'2023-04-20', 'time':'15:00', 'from': 'ETH', 'quantity_from': 345, 'To': '€', 'quantity_to': 567 },
        {'id':3,'date':'2023-03-15', 'time':'20:00', 'from': 'ETH', 'quantity_from': 567, 'To': '€', 'quantity_to': 234 }
    ]
    return render_template ("index.html", datos=datos_prueba )
#rutas inicio, compra y estado 