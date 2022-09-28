from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/productos/', methods=['GET'])
def productos():
    if request.method == 'GET':
        return 'metodo GET'
    else:
        return 'Se recibe la informacion desde un metodo POST'
@app.route('/descuentos/')
def descuentos():
    return render_template('descuentos.html')