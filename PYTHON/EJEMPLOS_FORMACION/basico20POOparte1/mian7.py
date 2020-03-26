###EN CONSTRUCCION

class Prenda():
    
    def __init__(self):
        
        self.codProd= -1
        self.nomProd =""
        self.marca =""
        self.modelo =""
        self.talla =""
        self.color =""
        self.sexo =""
        self.precio = -1

#end class Prenda

prenda = Prenda()

lista = []

registrar = True

while registrar:

    print('''
    
    Indica la Opción :
    
    1 - Registrar un producto
    2 - Consultar un producto
    3 - Salir de la aplicación
    
    ''')
    
    opcion = input("Opción : ")
    
    if opcion == 1:
        prenda.codProd = input("Indica el código de producto : ")
        prenda.nomProd = input("Indica el nombre del producto : ")
        prenda.marca = input("Indica la marca del producto : ")
        prenda.modelo = input("Indica el modelo del producto : ")
        prenda.talla = input("Indica la talla del producto : ")
        prenda.color = input("Indica el color del producto : ")
        prenda.sexo = input("Indica H para hombre, M para mujer : ")
        prenda.precio = input("Indica el precio del producto : ")
        
        lista.append(prenda)
        
        with open ("prendas.txt" , "a+") as listaPrendas:
            listaPrendas.write(prenda.codProd + ",")
            listaPrendas.write(prenda.nomProd + ",")
            listaPrendas.write(prenda.marca + ",")
            listaPrendas.write(prenda.modelo + ",")
            listaPrendas.write(prenda.talla + ",")
            listaPrendas.write(prenda.color + ",")
            listaPrendas.write(prenda. sexo + ",")
            listaPrendas.write(prenda.precio)                       
            listaPrendas.write("\n")
        
        print("Producto registrado")
    
    elif opcion == 2:
        print("Opcion en construccion")

    elif opcion == 3:
        print("Fin de la aplicación")
        registrar = False