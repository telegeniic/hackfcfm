from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def home():
    return render_template('inicio.html')

@app.route('/registro')
def registrar():
    return '<h1>Pagina de registro</h1>'