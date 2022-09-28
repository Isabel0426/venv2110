from flask import Flask
app = Flask(__name__)
@app.route('/articulo/<string:id>')
def mostrar_articulo(id):
    #return "Stock del articulo {}".format(id)
    #return "Stock del articulo: "+str(id)
    return "Stock del articulo: "+(id)