class Coche():
    
    def __init__(self, id_producto="", marca="", modelo="", color="", motor="", precio="", forma_pago = ""):
        
        self.id = id_producto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.precio = precio
        self.forma_pago = forma_pago
        
    def __str__(self):
        print(self.id + " , " + self.marca + " , " + self.modelo + " , " + self.color + " , " + self.motor + " , " + self.precio + "," + self.forma_pago)
        
        
