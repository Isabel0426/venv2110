import email
from email.headerregistry import Address
from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SubmitField ,EmailField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    email = EmailField('Mailing Address',validators= [DataRequired(message ='favor ingresar email')])
    Mensaje = TextAreaField('Mensaje')
    enviar = SubmitField('Iniciar Sesión')