class Receta:

    #Constructor
    def __init__(self, id, titulo, resumen, ingredientes, preparacion, tiempo, imagen, autor, categoria):
        self.id=id
        self.titulo=titulo
        self.resumen=resumen
        self.ingredientes=ingredientes
        self.preparacion=preparacion
        self.tiempo=tiempo
        self.imagen=imagen
        self.autor=autor
        self.categoria=categoria
    #Setter's
    def setId(self, id):
        self.id=id

    def setTitulo(self, titulo):
        self.titulo=titulo

    def setResumen(self, resumen):
        self.resumen=resumen
        
    def setIngredientes(self, ingredientes):
        self.ingredientes=ingredientes

    def setPreparacion(self, preparacion):
        self.preparacion=preparacion

    def setTiempo(self, tiempo):
        self.tiempo=tiempo

    def setImagen(self, imagen):
        self.imagen=imagen

    def setAutor(self, autor):
        self.autor=autor

    def setCategoria(self, categoria):
        self.categoria=categoria
    #Getter's
    def getId(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def getResumen(self):
        return self.resumen

    def getIngredientes(self):
        return self.ingredientes
    
    def getPreparacion(self):
        return self.preparacion

    def getTiempo(self):
        return self.tiempo

    def getImagen(self):
        return self.imagen

    def getAutor(self):
        return self.autor

    def getCategoria(self):
        return self.categoria