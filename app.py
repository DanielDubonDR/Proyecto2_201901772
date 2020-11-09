from flask import Flask, render_template, jsonify, request, redirect, session
from flask_cors import CORS
import datetime
#------------------------------------IMPORTANDO CLASES DONDE ALMACENO DATOS-----------------------------------------
from Datos.Usuario import Usuario
from Datos.Receta import Receta
from Datos.Comentario import Comentario
from Datos.Reaccion import Reaccion

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
ingredientes2="2 lb. de carne al gusto#1 chile guaque seco#2 onzas de ajonjolí#1 rajita de canela#1 chile pasa seco#4 tomates#2 onzas de pepitoria verde#1 cebolla#4 pimientas gordas#3 dientes de ajo#8 piezas de pan francés frío o harina de arroz#2 clavos de olor#½ Lb. de ejotes#½ Lb. de papas medianas#Sal y pimienta al gusto"
preparacion2="Primero, para el Pepián Negro, colocar en una olla la carne a cocer dentro del litro del agua.#Antes de que esté en su punto, agregar las verduras para su cocimiento.#Entonces, aparte en un comal, poner a dorar los chiles, el miltomate, el tomate, la cebolla, el ajonjolí, pepitoria, los dientes de ajo, la rajita de canela y la cáscara de plátano.#Después de que todos los ingredientes se hayan dorado perfectamente, licuar con un poco del caldo donde se ha cocido la carne.#Luego, ese licuado se pone a hervir y espesar junto con el manojo de cilantro, por espacio de 30 minutos.#Seguidamente, dejar caer la carne y las verduras, para que los sabores se mezclen entre sí y se deja hervir hasta espesar.#Para el Pepián Rojo debe omitirse en chile guaque y la cáscara de plátano, y agregarle más tomate, achiote y chile pimiento.#Finalmente, puede acompañarse con arroz blanco y un par de deliciosas tortillas"
ingredientes3="2 libras de pavo cortado en pedazos grandes#Media libra de tomate#4 onzas de miltomate#2 chiles guaques grandes#1 chile pasa grande#1 chile pimiento rojo grande#6 dientes de ajo grandes#1 cebolla mediana#4 ramas de cilantro"\
"#10 ramas de hierbabuena#Media onza de ajonjolí#4 granos de pimienta gorda o pimienta de chapa#4 a 5 granos de pimienta#1 onza de pepitoria#Tallos de cebolla#Achiote#Sal#Chile cobanero en polvo"
preparacion3="Primero, cocer el pavo con un poco de sal y un ramo hecho con tallos de cebolla, hierbabuena y cilantro en suficiente agua.#Asegurarse de que el agua cubra la carne ya que habrá de hervir y una parte se consumirá.#Para hacer el recado, primero dorar la pepitoria, el ajonjolí y los granos de pimienta."\
"#Asar el chile pimiento, los chiles, ajo, cebolla, el tomate y el miltomate.#Luego, licuar en seco el recado y colarlo.#Retirar el ramo con el que se cocinó el pavo y agregar el recado."\
"#Hervir durante 10 minutos y sazonar con un poco de sal, achiote y chile cobanero al gusto.#Cuidar que el pavo no se recueza.#Finalmente, servir en pedazos grandes con un poco de arroz, tortillas o tamalitos al gusto."

resumen2="Es un platillo tradicional guatemalteco de origen kaqchiquel, propio del departamento de Chimaltenango. Su origen es prehispánico y se servía en las ceremonias religiosas mayas. El pepián es un recado que puede prepararse con costilla de res, carne de cerdo, con pollo, o una mezcla las distintas carnes."
resumen3="El Kak’ik es conocido como caldo colorado de pavo o chunto, tradicional del departamento de Cobán, Guatemala. Es una comida ancestral de ascendencia prehispánica, por eso tiene el color rojo que rememora en alguna medida la sangre ritual de los antepasados en sus ceremonias."
Recetas.append(Receta("0","Cochinita Pibil",resumen1,ingredientes1,preparacion1,"1 hora","https://dam.cocinafacil.com.mx/wp-content/uploads/2019/08/tacos-de-cochinita.jpg","Daniel","Comida Mexicana"))
Recetas.append(Receta("1","Pepián",resumen2,ingredientes2,preparacion2,"2 horas","https://img-global.cpcdn.com/recipes/c4361919b103df7a/1200x630cq70/photo.jpg","Reginaldo","Platillo típico"))
Recetas.append(Receta("2","Kak'ik",resumen3,ingredientes3,preparacion3,"1 hora y 30 minutos","https://i.pinimg.com/originals/25/00/39/25003904d6b783d8645206af2d936b2c.jpg", "Sulvey","Platillo tipico"))

#--------------------------------------------------COMENTARIOS-----------------------------------------------------------
x = datetime.datetime.now()
fechActual=x.strftime("%b")+" "+x.strftime("%d")+", "+x.strftime("%Y")+", "+x.strftime("%I")+":"+x.strftime("%M")+" "+x.strftime("%p")

Comentarios=[]
Comentarios.append(Comentario("0","Daniel","Me gusta esta receta, la prepararé",fechActual))
Comentarios.append(Comentario("0","Reginaldo","Se ve delicioso",fechActual))
Comentarios.append(Comentario("1","Gatito Master","Me gusta esta receta, la prepararé",fechActual))
Comentarios.append(Comentario("2","Reginaldo","Me gusta esta receta, la prepararé",fechActual))

#---------------------------------------------------REACCIONES------------------------------------------------------------
nReaccion=2
Reacciones=[]
Reacciones.append(Reaccion("0","ME GUSTA","https://img.icons8.com/color/18/000000/facebook-like.png", 2, None))
Reacciones.append(Reaccion("1","NO ME GUSTA","https://img.icons8.com/color/18/000000/thumbs-down.png", 1, None))

dReactions=[]
dReactions.append(Reaccion("0",None,None,None,"0"))
dReactions.append(Reaccion("1",None,None,None,"0"))
dReactions.append(Reaccion("1",None,None,None,"1"))
dReactions.append(Reaccion("1",None,None,None,"1"))
dReactions.append(Reaccion("1",None,None,None,"1"))

#--------------------------------------------------FUNCIONES-----------------------------------------------------------
def validarCredenciales(user, password):
    for User in Usuarios:
        if User.getUsuario()==user and User.getContrasena()==password:
            return User
    return None

def validarUsuario(user):
    for User in Usuarios:
        if User.getUsuario()==user:
            return True
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
            idd=recipe.getId()
            title=recipe.getTitulo()
            resumen=recipe.getResumen()
            ingredientes=recipe.getIngredientes()
            preparacion=recipe.getPreparacion()
            tiempo=recipe.getTiempo()
            imagen=recipe.getImagen()
            categoria=recipe.getCategoria()
            autor=recipe.getAutor()
    if 'logueado' in session:
        return render_template('recetas/recipe.html', uss=session['logueado'], titulo=title, resumen=resumen, ingredientes=ingredientes.split("#"), preparacion=preparacion.split("#"), imagen=imagen, categoria=categoria, tiempo=tiempo, autor=autor, nombre=session['nombre'], tippo=session['tipo'], coment=Comentarios, identificador=idd, reacciones=Reacciones )
    return render_template('recetas/recipe.html',uss=None, titulo=title, resumen=resumen, ingredientes=ingredientes.split("#"), preparacion=preparacion.split("#"), imagen=imagen, categoria=categoria, tiempo=tiempo, autor=autor, coment=Comentarios, identificador=idd, reacciones=Reacciones)

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
    a=0
    for s in Reacciones:        
        a+=s.getContador()
    return render_template('dashboard/dashboard.html', nombre=session['nombre'], nrecetas=len(Recetas), nusuarios=len(Usuarios), ncomentarios=len(Comentarios), reactions=a)

@app.route('/dashboard/recetasPublicadas')
def recetasPublicadas():
    return render_template('dashboard/recetasPublicadas.html', nombre=session['nombre'], nrecetas=len(Recetas), recipes=Recetas)

@app.route('/dashboard/recetaReporte')
def reporteRecetas():
    return render_template('dashboard/reporteRecetas.html', nombre=session['nombre'], nrecetas=len(Recetas), recipes=Recetas)

@app.route('/dashboard/editarReceta/<string:ID>')
def editarReceta(ID):
    temp=Recetas[int(ID)]
    return render_template('dashboard/editarRecetas.html', nombre=session['nombre'], recipe=temp)

@app.route('/dashboard/recetas/editar/<string:IDA>', methods=['PUT'])
def edit(IDA):
    nuevo=Receta(IDA,request.json['titulo'],request.json['resumen'],request.json['ingredientes'],request.json['preparacion'], request.json['tiempo'], request.json['imagen'], Recetas[int(IDA)].getAutor(), request.json['categoria'])
    Recetas[int(IDA)]=nuevo
    return jsonify({'message':'Se modifico la receta'})

@app.route('/dashboard/recetas/eliminar/<string:ID>')
def eliminarReceta(ID):
    for i in range(len(Recetas)):
        if ID == Recetas[i].getId():
            del Recetas[i]
            return redirect("/dashboard/recetasPublicadas")

@app.route('/dashboard/usuarios')
def usuariosRegistrados():
    return render_template('dashboard/usuarios.html', nombre=session['nombre'], nusuarios=len(Usuarios), users=Usuarios) 

@app.route('/dashboard/usuarios/registrar')
def usuariosAgregar():
    return render_template('dashboard/agregarAdmin.html', nombre=session['nombre']) 

@app.route('/dashboard/newUser/<string:usuario>', methods=['POST'])
def agregarAdmin(usuario):
    encontrado=validarUsuario(usuario)
    if encontrado==False:
        n=Usuario(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['password'],0)
        Usuarios.append(n)
        return jsonify({'message':'Se registro correctamente'})
    else:
        return jsonify({'message':'Este usuario ya esta registrado'}) 

@app.route('/dashboard/comentarios')
def mostrarComentarios():
    return render_template('dashboard/comentarios.html', nombre=session['nombre'], recipes=Recetas, ncomentarios=len(Comentarios))

@app.route('/dashboard/vercomentarios/<string:ID>')
def verComentarios(ID):
    title=Recetas[int(ID)].getTitulo()
    return render_template('dashboard/verComentarios.html', nombre=session['nombre'], comentarios=Comentarios, ident=ID, title=title) 

@app.route('/dashboard/cargaMasiva', methods=['POST'])
def cargaMasiva():
    global id
    a=Receta(str(id),request.json['titulo'],request.json['resumen'],request.json['ingredientes'],request.json['procedimiento'],request.json['tiempo'],request.json['url'],request.json['autor'],"SIN CATEGORIA")
    Recetas.append(a)
    id=id+1
    return jsonify({'message':'Se agregaron las recetas'}) 

@app.route('/dashboard/agregarReacciones')
def agregarReacciones():
    return render_template('dashboard/reacciones.html', nombre=session['nombre'], reacciones=Reacciones)

@app.route('/dashboard/addReaccion', methods=['POST'])
def addReacciones():
    global nReaccion
    s=Reaccion(str(nReaccion),request.json['reaccion'],request.json['url'],0, None)
    nReaccion=nReaccion+1
    Reacciones.append(s)
    return jsonify({'message':'Se agrego las reacción'}) 

@app.route('/reaccion/add', methods=['POST'])
def addReact():
    aux=request.json['idReaccion']
    r=Reacciones[int(aux)].getContador()+1
    Reacciones[int(aux)].setContador(r)
    s=Reaccion(request.json['idReaccion'],None,None,None,request.json['idReceta'])
    dReactions.append(s)
    return jsonify({'message':'Se agrego las reacción'}) 
#---------------------------------------------------COMENTARIO------------------------------------------------
@app.route('/comentario/add/<string:ID>', methods=['POST'])
def addComentario(ID):
    nuevo=Comentario(ID,session['nombre'],request.json['comentario'],fechActual)
    Comentarios.append(nuevo)
    return jsonify({'message':'Se agrego el comentario'})

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
            if usuario.getTipo()==0:
                return redirect('/dashboard')
            else:
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