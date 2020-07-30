#Crear una aplicación de consola que permita registrar y listar libros y clientes
#usando un diseño modular

from menus import *
from listados import listar_libros

libros = [] # Array para guardar los libros que se vayan registrando
opcionInsertada = -1

while opcionInsertada != 3:
    opcionInsertada = menu_principal()
    if opcionInsertada == 1:
        #registrar un libro
        libro = menu_insertar_libro()
        #La variable libro captura el return de la funcion menu_insertar_libro()
        libros.append(libro)
    elif opcionInsertada == 2:
        listar_libros(libros)
    else:
        print("Fin del programa")