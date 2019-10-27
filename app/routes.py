from flask import render_template, request
from app import app, db
from app.forms import LoginForm
from app.models import * 
from sqlalchemy.orm import lazyload, joinedload

ent700 = []
Entradas = ['700', '800', '900', '1000', '1100', '1200', '1300']
Salidas = ['800', '900', '1000', '1100', '1200', '1300', '1400', '1500']

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/agenda')
def dropdown():
    
    return render_template('agenda.html', Entradas=Entradas, Salidas=Salidas)

@app.route('/submitagenda', methods=['POST'])
def submited():
    return render_template('agenda.html', Entradas=Entradas, Salidas=Salidas)
