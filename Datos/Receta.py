class Receta:

    #Constructor
    def __init__(self, titulo, resumen, ingredientes, preparacion, tiempo, imagen, autor):
        self.titulo=titulo
        self.resumen=resumen
        self.ingredientes=ingredientes
        self.preparacion=preparacion
        self.tiempo=tiempo
        self.imagen=imagen
        self.autor=autor
    
    #Setter's

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
    #Getter's

    def getTitulo(self):
        return titulo

    def getResumen(self):
        return resumen

    def getIngredientes(self):
        return ingredientes
    
    def getPreparacion(self):
        return preparacion

    def getTiempo(self):
        return tiempo

    def getImagen(self):
        return imagen

    def getAutor(self):
        return autor