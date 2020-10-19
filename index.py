from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

#Importando las clases donde almaceno datos
from Datos.Usuario import Usuario
from Datos.Receta import Receta

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('login/login.html')

@app.route('/registrar.html')
def registar():
    return render_template('login/registrar.html')

if __name__=='__main__':
    app.run(debug=True)