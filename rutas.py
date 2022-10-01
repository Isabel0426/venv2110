from flask import Flask, render_template,flash, redirect,url_for
from forms import FormInicio
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
@app.route('/forms',methods=('GET','POST'))
def forms():
    form = FormInicio()
    if(form.validate_on_submit()):
        return redirect(url_for('gracias'))
    return render_template('form.html', titulo='Iniciar Sesión', form=form)
@app.route('/gracias')
def gracias():
    return render_template('gracias.html')