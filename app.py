from flask import Flask, render_template
app = Flask(__name__)
@app.route('/formulario/')
def index():
    return render_template('sesion8.html')
#GRUPO 2110