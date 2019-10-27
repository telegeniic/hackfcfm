from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    correo = StringField('Correo', validators=[DataRequired()])
    password = PasswordField('Contrasenna', validators=[DataRequired()])
    recuerdame = BooleanField('Recuerdame')
    subir = SubmitField('Iniciar Secion')