from flask import render_template, request
from app import app, db
from app.forms import LoginForm
from app.models import * 
from sqlalchemy.orm import lazyload, joinedload

clases = ["Calculo Diferencial", "Topicos", "Fisica", "Geometria", "Progra Estruct", "Lab Progra", "Lab Fisica"]
primera = [clases[0], clases[0], clases[0], clases[0], clases[0]]
segunda = [clases[1], clases[1], clases[1], clases[1], clases[1]]
tercera = [clases[2], clases[2], clases[2], clases[2], clases[2]]
cuarta = [clases[3], clases[3], clases[3], clases[3], clases[3]]
quinta = [clases[4], clases[4], clases[4], clases[4], clases[4]]
sexta = [clases[5], clases[6]]
septima = [clases[5], clases[6]]
Entradas = ['700', '800', '900', '1000', '1100', '1200', '1300']
Salidas = ['800', '900', '1000', '1100', '1200', '1300', '1400', '1500']

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/agenda')
def dropdown():
    
    return render_template('agendapre.html', Entradas=Entradas, Salidas=Salidas)

@app.route('/submitagenda', methods=['POST'])

def submited():
    entrada = request.form.get("Entradas")
    salida = request.form.get("Salidas")
    entrada = int(entrada)
    salida = int(salida)
    return render_template('agenda.html',entrada=entrada, salida=salida, Entradas=Entradas, Salidas=Salidas, primera=primera,segunda=segunda,tercera=tercera,cuarta=cuarta,quinta=quinta,sexta=sexta,septima=septima)
