class Coche():
    
    def __init__(self, id_producto="", marca="", modelo="", color="", motor="", precio=""):
        
        self.id = id_producto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.precio = precio
        
    def __str__(self):
        print(self.id + " , " + self.marca + " , " + self.modelo + " , " + self.color + " , " + self.motor + " , " + self.precio)
        
        
