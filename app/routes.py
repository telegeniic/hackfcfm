from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/signin')
def registrar():
    return '<h1>Pagina de registro</h1>'

@app.route('/login')
def inicarSecion():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/agenda')
def dropdown():
    Entradas = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 pm', '1:00 pm']
    Salidas = ['8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 pm', '1:00 pm', '2:00 pm', '3:00 pm']
    return render_template('agenda.html', Entradas=Entradas, Salidas=Salidas)