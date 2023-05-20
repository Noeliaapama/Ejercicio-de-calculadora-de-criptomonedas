from flask_classic import app

@app.route("/")
def hello():
    return "hola caracola"