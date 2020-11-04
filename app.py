from flask import Flask, render_template, jsonify, request, redirect, session
from flask_cors import CORS
import time
#------------------------------------IMPORTANDO CLASES DONDE ALMACENO DATOS-----------------------------------------
from Datos.Usuario import Usuario
from Datos.Receta import Receta

#---------------------------------------------USUARIOS PRUEBA-------------------------------------------------------
Usuarios=[]
Usuarios.append(Usuario('Usuario','Maestro','admin','admin',0))
Usuarios.append(Usuario('Daniel','Reginaldo','daniel','123',1))

#----------------------------------------------VARIABLES GLOBALES---------------------------------------------------
global id
id=3

#-------------------------------------------RECETAS PREDETERMIANDAS-------------------------------------------------
Recetas=[]
resumen1="Es un guiso correspondiente a la gastronomía de Yucatán,​ basado en carne de cerdo adobada en achiote, envuelta en hoja de plátano y cocida dentro de un horno de tierra usando una técnica prehispánica conocida como pib."
preparacion1="Enjuaga la carne y córtala en trozos."\
"#Licúa el jugo de naranja con la cebolla, el vinagre y el achiote."\
"#Pon a cocer la carne con la mezcla en olla de presión por 30 minutos."\
"#Mientras, corta la cebolla en julianas, saltéala en aceite de oliva"\
"#Ponla en un recipiente con el vinagre, un poco de sal y orégano."\
"#Corta el chile habanero en rebanadas finas, ponle el jugo de limón, un poco de agua y sal al gusto. #Sirve los tacos con las cebollitas y una rebanada de habanero."
ingredientes1="Para la carne#1 kilo de pulpa de cerdo#1 litro de jugo de naranja"\
"#1/4 de cebolla#1/2 taza de vinagre de manzana#100 g de pasta de achiote"\
"#Chile habanero#1 limón (el jugo)#Para las cebollas"\
"#1 cebolla morada#4 cucharadas de aceite de oliva"\
"#1/4 de taza de vinagre#1 cucharadita de orégano#Sal"
resumen2="Es un platillo tradicional guatemalteco de origen kaqchiquel, propio del departamento de Chimaltenango. Su origen es prehispánico y se servía en las ceremonias religiosas mayas. El pepián es un recado que puede prepararse con costilla de res, carne de cerdo, con pollo, o una mezcla las distintas carnes."
resumen3="El Kak’ik es conocido como caldo colorado de pavo o chunto, tradicional del departamento de Cobán, Guatemala. Es una comida ancestral de ascendencia prehispánica, por eso tiene el color rojo que rememora en alguna medida la sangre ritual de los antepasados en sus ceremonias."
Recetas.append(Receta("0","Cochinita Pibil",resumen1,ingredientes1,preparacion1,"1 hora","https://dam.cocinafacil.com.mx/wp-content/uploads/2019/08/tacos-de-cochinita.jpg","Daniel","Comida Mexicana"))
Recetas.append(Receta("1","Pepián",resumen2,"none","none","2 horas","https://img-global.cpcdn.com/recipes/c4361919b103df7a/1200x630cq70/photo.jpg","Reginaldo","Platillo típico"))
Recetas.append(Receta("2","Kak'ik",resumen3,"none","none","1 hora y 30 minutos","https://i.pinimg.com/originals/25/00/39/25003904d6b783d8645206af2d936b2c.jpg", "Sulvey","Platillo tipico"))

#--------------------------------------------------FUNCIONES-----------------------------------------------------------
def validarCredenciales(user, password):
    for User in Usuarios:
        if User.getUsuario()==user and User.getContrasena()==password:
            return User
            break
    return None

def validarUsuario(user):
    for User in Usuarios:
        if User.getUsuario()==user:
            return True
            break
    return False

#------------------------------------------------------API-REST-----------------------------------------------------
app = Flask(__name__)
CORS(app)
app.secret_key=b'xdycghzubhu55h&hh(j)u_kgbhb#$f'

@app.route('/')
def home():
    if 'logueado' in session:
        return render_template('login/principal.html', Recetas=Recetas, uss=session['logueado'], nombre=session['nombre'], tippo=session['tipo'])
    return render_template('login/principal.html', Recetas=Recetas, uss=None)


#------------------------------------------------------CARGAR RECETA DETALLADA-----------------------------------------------------
@app.route('/receta/<string:ID>')
def verReceta(ID):
    title=""
    resumen=""
    ingredientes=""
    preparacion=""
    tiempo=""
    imagen=""
    categoria=""
    autor=""
    for recipe in Recetas:
        if recipe.getId()==ID:
            title=recipe.getTitulo()
            resumen=recipe.getResumen()
            ingredientes=recipe.getIngredientes()
            preparacion=recipe.getPreparacion()
            tiempo=recipe.getTiempo()
            imagen=recipe.getImagen()
            categoria=recipe.getCategoria()
            autor=recipe.getAutor()
    if 'logueado' in session:
        return render_template('recetas/recipe.html', uss=session['logueado'], titulo=title, resumen=resumen, ingredientes=ingredientes.split("#"), preparacion=preparacion.split("#"), imagen=imagen, categoria=categoria, tiempo=tiempo, autor=autor, nombre=session['nombre'], tippo=session['tipo'])
    return render_template('recetas/recipe.html',uss=None, titulo=title, resumen=resumen, ingredientes=ingredientes.split("#"), preparacion=preparacion.split("#"), imagen=imagen, categoria=categoria, tiempo=tiempo, autor=autor)

#-------------------------------------------------------------INGRESAR RECETA-------------------------------------------------------
@app.route('/ingresarReceta')
def ingresarReceta():
    return render_template('recetas/ingresar.html', uss=session['logueado'], tippo=session['tipo'], nombre=session['nombre'])

@app.route('/ingresarReceta/add', methods=['POST'])
def addReceta():
    global id
    nuevo=Receta(str(id),request.json['titulo'],request.json['resumen'],request.json['ingredientes'],request.json['preparacion'], request.json['tiempo'], request.json['imagen'], session['nombre'], request.json['categoria'])
    Recetas.append(nuevo)
    id=id+1
    return jsonify({'message':'Se agrego la receta'})

#-------------------------------------------------------------DASHBOARD-------------------------------------------------------
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html', nombre=session['nombre'], nrecetas=len(Recetas), nusuarios=len(Usuarios))

@app.route('/dashboard/recetasPublicadas')
def recetasPublicadas():
    return render_template('dashboard/recetasPublicadas.html', nombre=session['nombre'], nrecetas=len(Recetas), recipes=Recetas)

@app.route('/dashboard/editarReceta/<string:ID>')
def editarReceta(ID):
    temp=Recetas[int(ID)]
    return render_template('dashboard/editarRecetas.html', nombre=session['nombre'], recipe=temp)
#---------------------------------------------------MANEJO DE LOGIN------------------------------------------------
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        usuario = validarCredenciales(request.form['user'], request.form['pass'])
        if usuario != None:
            session['logueado'] = usuario.getUsuario()
            session['nombre']=usuario.getNombre()
            session['apellido']=usuario.getApellido()
            session['tipo']=usuario.getTipo()
            return redirect('/')
        else:
            error = 'Contrasena invalida'
            return render_template('login/login.html', error=error)
    if 'logueado' in session:
        return redirect('/')
    return render_template('login/login.html', error=error)

@app.route('/recuperar', methods=['POST', 'GET'])
def forgot():
    error = None
    p=None
    if request.method == 'POST':
        usuario = validarUsuario(request.form['user'])
        if usuario == True:
            for User in Usuarios:
                if User.getUsuario()==request.form['user']:
                    p=User.getContrasena()
        else:
            error = 'Usuario no encontrado'
    return render_template('login/recuperar.html', error=error, p=p)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logueado', None)
    return redirect('/')

#--------------------------------------------REGISTRAR------------------------------------------

@app.route('/registrar', methods=['POST', 'GET'])
def registar():
    error=False
    if request.method == 'POST':
        verificar=validarUsuario(request.form['usuario'])
        if verificar==False:
            global Usuarios
            n = Usuario(request.form['nombre'],request.form['apellido'],request.form['usuario'],request.form['contrasena'],1)
            Usuarios.append(n)
            '''a="r"
            return render_template('login/registrar.html', error=a)'''
            return redirect('login')
        else:
            return render_template('login/registrar.html', error=True)
    return render_template('login/registrar.html')

#------------------------------------------------MODIFICAR PERFIL-----------------------------------------------
@app.route('/perfil')
def perfil():
    if 'logueado' in session:
        return render_template('perfil/perfil.html',uss=session['logueado'], nombre=session['nombre'], tippo=session['tipo'], apellido=session['apellido'])

@app.route('/perfil/modificar')
def perfilm():
    if 'logueado' in session:
        return render_template('perfil/perfilm.html',uss=session['logueado'], nombre=session['nombre'], tippo=session['tipo'], apellido=session['apellido'])

@app.route('/perfil/password')
def password():
    if 'logueado' in session:
        return render_template('perfil/perfilp.html',uss=session['logueado'], nombre=session['nombre'], tippo=session['tipo'], apellido=session['apellido'])

@app.route('/perfil/modificar/<string:usuario>', methods=['PUT'])
def ActualizarDatos(usuario):
    encontrado=validarCredenciales(session['logueado'], usuario)
    if encontrado!=None:
        if encontrado.getUsuario()!=request.json['usuario']:
            if validarUsuario(request.json['usuario'])==False:
                encontrado.setNombre(request.json['nombre'])
                encontrado.setApellido(request.json['apellido'])
                encontrado.setUsuario(request.json['usuario'])
                session['nombre']=request.json['nombre']
                session['apellido']=request.json['apellido']
                session['logueado']=request.json['usuario']
                return jsonify({'message':'Se actualizaron los datos exitosamente'})
            else:
                return jsonify({'message':'Este usuario ya esta registrado'})
        else:
            encontrado.setNombre(request.json['nombre'])
            encontrado.setApellido(request.json['apellido'])
            session['nombre']=request.json['nombre']
            session['apellido']=request.json['apellido']
            return jsonify({'message':'Se actualizaron los datos exitosamente'})
    else:
        return jsonify({'message':'Contraseña invalida'})

@app.route('/perfil/password/<string:usuario>', methods=['PUT'])
def ActualizarPass(usuario):
    encontrado=validarCredenciales(usuario, request.json['contrasenaActual'])
    if encontrado!=None:
        encontrado.setContrasena(request.json['contrasenaNueva'])
        return jsonify({'message':'Se actualizó la contraseña'})
    else:
        return jsonify({'message':'Contraseña actual invalida'})
#----------------------------------------------ERROR 404--------------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('extras/404.html'), 404

if __name__=='__main__':
    app.run(debug=True)