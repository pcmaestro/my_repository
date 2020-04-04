class Revista():
    
    def __init__(self):
        self.titulo = ""
        self.precio = 0.0
        self.tema = ""
        
    def a_texto(self):
        return "Titulo : {} Precio : {} Tema : {}".format(self.titulo, self.precio, self.tema)