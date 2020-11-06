class Comentario:

    def __init__(self, id, usuario, texto, fecha):
        self.id=id
        self.usuario=usuario
        self.texto=texto
        self.fecha=fecha

    def setId(self, id):
        self.id=id

    def setUsuario(self, usuario):
        self.usuario=usuario

    def setTexto(self, texto):
        self.texto=texto
    
    def setFecha(self, fecha):
        self.fecha=fecha

    def getId(self):
        return self.id
    
    def getUsuario(self):
        return self.usuario
    
    def getTexto(self):
        return self.texto

    def getFecha(self):
        return self.fecha