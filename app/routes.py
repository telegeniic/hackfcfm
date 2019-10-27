from flask import render_template, request
from app import app
from app.forms import LoginForm
from app.generate import Generate
from app.llenar import llenar

Entradas = ['7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '1:00']
Salidas = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']

@app.route('/')
@app.route('/index')
def home():
    llenar()
    return render_template('index.html')

@app.route('/agenda')
def dropdown():
    
    return render_template('agenda.html', Entradas=Entradas, Salidas=Salidas)

@app.route('/submitagenda', methods=['POST'])
def submited():
    Hi = request.form.get("Entradas")
    Hf = request.form.get("Salidas")
    if (Hi == Hf):
        print("problema")
    return render_template('agenda.html', Entradas=Entradas, Salidas=Salidas)
