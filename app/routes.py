from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def home():
    return "Hola mundo"