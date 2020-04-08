class Revista():
    
    def __init__(self, titulo = "", precio = 10, tema = "" , id = 0):
        self.titulo = titulo
        self.precio = precio
        self.tema = tema
        self.id = id
    
        
    def a_texto(self):
        return "titulo: {} precio: {} tema: {}".format(self.titulo,self.precio,self.tema)
    