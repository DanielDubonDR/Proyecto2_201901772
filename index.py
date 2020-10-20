from flask import Flask, render_template, jsonify, request, redirect, session
from flask_cors import CORS

#Importando las clases donde almaceno datos
from Datos.Usuario import Usuario
from Datos.Receta import Receta

#Creando los primeros usuarios
Usuarios=[]
Usuarios.append(Usuario('Usuario','Maestro','admin','admin',0))
Usuarios.append(Usuario('Daniel','Reginaldo','dd','456',1))
Usuarios.append(Usuario('Anahi','Dubon','Anahi','27',1))

#Creando las primeras recetas
Recetas=[]
resumen1="Es un guiso correspondiente a la gastronomía de Yucatán,​ basado en carne de cerdo adobada en achiote, envuelta en hoja de plátano y cocida dentro de un horno de tierra usando una técnica prehispánica conocida como pib."
resumen2="Es un platillo tradicional guatemalteco de origen kaqchiquel, propio del departamento de Chimaltenango. Su origen es prehispánico y se servía en las ceremonias religiosas mayas. El pepián es un recado que puede prepararse con costilla de res, carne de cerdo, con pollo, o una mezcla las distintas carnes."
resumen3="El Kak’ik es conocido como caldo colorado de pavo o chunto, tradicional del departamento de Cobán, Guatemala. Es una comida ancestral de ascendencia prehispánica, por eso tiene el color rojo que rememora en alguna medida la sangre ritual de los antepasados en sus ceremonias."
Recetas.append(Receta("Cochinita Pibil",resumen1,"none","none","none","https://okdiario.com/img/recetas/2016/11/13/cochinita-pibil.jpg"))
Recetas.append(Receta("Pepián",resumen2,"none","none","none","https://www.guatemala.com/fotos/2019/09/Convocatoria-para-participar-en-el-Festival-del-Pepian-2019-en-la-Ciudad-de-Guatemala1.jpg"))
Recetas.append(Receta("Kak'ik",resumen3,"none","none","none","https://aprende.guatemala.com/wp-content/uploads/2016/10/Receta-de-Kaqik-guatemalteco.jpg"))

#Funciones
def validarCredenciales(user, password):
    for User in Usuarios:
        if User.getUsuario()==user and User.getContrasena()==password:
            datosUsuario=User
            return User
    return None

#API-REST
app = Flask(__name__)
CORS(app)
app.secret_key=b'xdycghzubhu55h&hh(j)u_kgbhb#$f'

@app.route('/')
def home():
    if 'logueado' in session:
        return render_template('login/principal.html', Recetas=Recetas, uss=session['logueado'])
    return render_template('login/principal.html', Recetas=Recetas, uss=None)

@app.route('/registrar')
def registar():
    return render_template('login/registrar.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        usuario = validarCredenciales(request.form['user'], request.form['pass'])
        if usuario != None:
            session['logueado'] = usuario.getUsuario()
            return redirect('/')
        else:
            error = 'Contrasena invalida'
            return render_template('login/login.html', error=error)
    if 'logueado' in session:
        return redirect('/')
    return render_template('login/login.html', error=error)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logueado', None)
    return redirect('login')

if __name__=='__main__':
    app.run(debug=True)