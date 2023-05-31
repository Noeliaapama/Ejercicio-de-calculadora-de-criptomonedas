from flask import Flask, session
from flask_classic.config import SECRET_KEY

app=Flask(__name__, instance_relative_config=True)

#app.config.from_object("config")
app.config.from_object(__name__)
# Se le dice a flaks que use el secret para cifrar la sesión
app.secret_key = SECRET_KEY #inserta tu secret key creada desde https://randomkeygen.com/

BBDD= "data/mov_criptos.sqlite"


from flask_classic.routes import *

