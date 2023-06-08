class Coche():
    largo = 250
    ancho = 120
    ruedas = 4
    enmarcha = False
    
    def arrancar(self):
        self.enmarcha = True
        
    def estado(self):
        
        if self.enmarcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"
