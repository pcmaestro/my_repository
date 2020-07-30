class Anuncio():
    
    def __init__(self, marca = "", modelo = "", color = "", pantalla = "", memoria= "", anyo = 0, precio = 0, nombre = "", telefono = 0 , email = ""):
        
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.pantalla = pantalla
        self.memoria = memoria
        self.anyo = anyo
        self.precio = precio
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        print(self.marca, self.modelo, self.color, self.pantalla, self.memoria, self.anyo, self.precio, self.nombre, self.telefono, self.email)