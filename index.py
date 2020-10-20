from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

#Importando las clases donde almaceno datos
from Datos.Usuario import Usuario
from Datos.Receta import Receta

#Creando los primeros usuarios
Usuarios=[]
Usuarios.append(Usuario("Usuario","Maestro","admin","admin",0))
Usuarios.append(Usuario("Daniel","Reginaldo","456","465",1))

#Creando las primeras recetas
Recetas=[]
resumen1="Es un guiso correspondiente a la gastronomía de Yucatán,​ basado en carne de cerdo adobada en achiote, envuelta en hoja de plátano y cocida dentro de un horno de tierra usando una técnica prehispánica conocida como pib."
resumen2="Es un platillo tradicional guatemalteco de origen kaqchiquel, propio del departamento de Chimaltenango. Su origen es prehispánico y se servía en las ceremonias religiosas mayas. El pepián es un recado que puede prepararse con costilla de res, carne de cerdo, con pollo, o una mezcla las distintas carnes."
resumen3="El Kak’ik es conocido como caldo colorado de pavo o chunto, tradicional del departamento de Cobán, Guatemala. Es una comida ancestral de ascendencia prehispánica, por eso tiene el color rojo que rememora en alguna medida la sangre ritual de los antepasados en sus ceremonias."
Recetas.append(Receta("Cochinita Pibil",resumen1,"none","none","none","https://okdiario.com/img/recetas/2016/11/13/cochinita-pibil.jpg"))
Recetas.append(Receta("Pepián",resumen2,"none","none","none","https://www.guatemala.com/fotos/2019/09/Convocatoria-para-participar-en-el-Festival-del-Pepian-2019-en-la-Ciudad-de-Guatemala1.jpg"))
Recetas.append(Receta("Kak'ik",resumen3,"none","none","none","https://aprende.guatemala.com/wp-content/uploads/2016/10/Receta-de-Kaqik-guatemalteco.jpg"))

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('login/principal.html', Recetas=Recetas)

@app.route('/registrar.html')
def registar():
    return render_template('login/registrar.html')

@app.route('/login.html')
def login():
    return render_template('login/login.html')

if __name__=='__main__':
    app.run(debug=True)