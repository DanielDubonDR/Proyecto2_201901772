class Reaccion:

    #Constructor
    def __init__(self, id, reaccion, icono, contador):
        self.id=id
        self.reaccion=reaccion
        self.icono=icono
        self.contador=contador

    #Getter's
    def getId(self):
        return self.id
    
    def getUsuario(self):
        return self.reaccion

    def getContador(self):
        return self.contador
    
    def getIcono(self):
        return self.icono

    #Setter's

    def setNombre(self, id):
        self.id=id

    def setApellido(self, reaccion):
        self.reaccion=reaccion

    def setContador(self, contador):
        self.contador=contador

    def setContador(self, icono):
        self.icono=icono
