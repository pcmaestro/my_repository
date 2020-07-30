'''
    clases
'''
class Caballo():
    nombre = ""
    color = ""
    numero = 0
    posicion = 0
    
    #Esto es un constructor, que exige cosas cuando se instancie un objeto de la clase caballo
    def __init__(self, nombre, color, numero):
        self.nombre = nombre
        self.color = color
        self.numero = numero


    