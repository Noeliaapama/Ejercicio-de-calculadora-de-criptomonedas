from flask import Flask

app = Flask(__name__)

from flask_classic.routes import *
