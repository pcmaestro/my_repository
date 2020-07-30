
class Revista():
    
    def __init__(self, titulo = "", precio = 10, tema = "" , \
                 digital= False, frecuencia = "semanal", tipo = "standar", \
                 id = 0):
        self.titulo = titulo
        self.precio = precio
        self.tema = tema
        self.digital = digital
        self.frecuencia = frecuencia
        self.tipo = tipo
        self.id = id
    
        
    def a_texto(self):
        return "titulo: {} precio: {} tema: {}".format(self.titulo,self.precio,self.tema)
    