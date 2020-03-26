
import clases as cls

def menuPrincipal():
    print("Elije una opción\n")
    print("1- Insertar una prenda\n2- Listar prendas\n3- Insertar cliente\n4- Listar clientes\n5- Cerrar aplicación\n")
    introducido = input()
    if introducido.isnumeric():
        introducido_int = int(introducido)
        if introducido_int < 1 and introducido > 5:
            print("Opción no válida, elija opción entre 1 y 5\n")
        else:
            return introducido_int
    else:
        print("debes introducir un número\n")
        

def menuInsertarPrenda():
    print("Inserta las caracteristicas de la prenda\n")
    nuevaPrenda = cls.Prenda()
    print("indica el nombre de la prenda")
    nuevaPrenda.nombre = input()
    print("indica la talla de la prenda")
    nuevaPrenda.talla = input()
    print("indica el color de la prenda")
    nuevaPrenda.color = input()
    print("indica el tejido de la prenda")
    nuevaPrenda.tejido = input()
    print("indica si la prenda es de niño o de adulto ( N o A)")
    nuevaPrenda.adultoNino = input()
    print("indica si la prenda es de hombre o mujer (H o M)")
    nuevaPrenda.sexo = input()
    return nuevaPrenda

def menuInsertarCliente():
    print("Inserta los datos de un nuevo cliente\n")
    nuevoCliente = cls.Cliente()
    nuevoCliente.nombreCompleto = input("Indica el nombre completo del cliente : ")
    nuevoCliente.direccion = input("Indica la dirección completa del cliente : ")
    nuevoCliente.email = input("Indica el e-mail del cliente : ")
    return nuevoCliente
    
    