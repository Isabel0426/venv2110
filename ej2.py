from flask import Flask
app = Flask(__name__)
@app.route('/hola/')
@app.route('/hola/<string:nombre>')
@app.route('/hola/<string:nombre>/<string:apellido>/<int:edad>')
def hola(nombre="",apellido="",edad=""):
    if nombre and apellido:
        return "Hola {} {}, tienes {} años".format(nombre,apellido,edad)
    elif nombre:
        return "Hola, {}".format(nombre)
    else:
        return "Hola tripulantes"