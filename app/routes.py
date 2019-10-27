from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
    return render_template('inicio.html')

@app.route('/signin')
def registrar():
    return '<h1>Pagina de registro</h1>'

@app.route('/login')
def inicarSecion():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')