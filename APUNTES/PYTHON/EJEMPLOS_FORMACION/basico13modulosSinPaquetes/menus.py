'''
    modulo menus
'''

import clases as cls

def menu_principal():
    print("Inserta una opción")
    print("1- Registrar libro")
    print("2- Listar libros")
    print("3- Salir")
    introducido = input()
    if introducido.isnumeric():
        introducido_int = int(introducido)
        if introducido_int < 1 or introducido_int > 3:
            print("opcion no valida")
        else:
            return introducido_int
    else:
        print("debes introducir un número")
        
def menu_insertar_libro():
    print("Inserta los datos del nuevo libro")
    nuevo_libro = cls.Libro()
    #nuevo_libro tiene todo lo definido en la clase libro del modulo clases
    print("Introduce el título")
    nuevo_libro.titulo = input()
    print("Introduce el número de páginas")
    nuevo_libro.paginas = input()
    print("Introduce el precio")
    nuevo_libro.precio = input()
    return nuevo_libro # Aqui cortamos esta función


    