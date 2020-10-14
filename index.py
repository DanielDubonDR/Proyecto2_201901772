from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

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