from flask import Flask

app=Flask(__name__, instance_relative_config=True)

BBDD= "data/mov_criptos.sqlite"


from flask_classic.routes import *
