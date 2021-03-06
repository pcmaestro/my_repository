#Manera sencilla de indicar las propiedades de una clase
class Juguete1():
    nombre = ""
    precio = ""
    
#end juguete

patines = Juguete1()

patines.nombre = "patines"
patines.precio = 0

#Pero la forma habitual es hacerlo con un constructor de objetos

class Juguete2():
    def __init__(self):
        self.nombre = ""
        self.precio = 0
        self.cantidad = 12

#Podemos hacer que el constructor pida directamente los parámetros

class Juguete3():
    def __init__(self, nombre, precio):
        self.nombre_producto = nombre
        self.precio_producto = precio
        
juego = Juguete3("Parchis", 10)

print("El producto " + juego.nombre_producto + " vale " + 
      str(juego.precio_producto) + " euros")

#También podemos incluso hacer que el constructor pida expresamente los parámetros

class Juguete4():
    def __init__(self, nombre="", precio = 0):
        self.nombre_producto = nombre
        self.precio_producto = precio
        
juego2 = Juguete4(nombre= "Oca", precio= 15)

print("El producto " + juego2.nombre_producto + " vale " + 
    str(juego2.precio_producto) + " euros")
        


    