from flask import Flask ,render_template
from tkinter import *
#Importa a biblioteca flask

app = Flask(__name__)
#Inicia o projeto Flask

@app.route("/") #Define uma rota padrão
def home():#Define a função principal
    return render_template('index.html') #Renderiza o template index.html


