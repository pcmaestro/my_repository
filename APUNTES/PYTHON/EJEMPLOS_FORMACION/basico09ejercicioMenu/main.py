#Aplicación de consola que permita registrar y listar libros

#Cada libro tendrá un título, un precio y número de páginas

class Libro():
    titulo = ""
    precio = 0.0
    paginas = 0
    
libros = []

opcionInsertada = -1

while opcionInsertada != 3:
    print("Introduce una opcion")
    print("1- Insertar libro")
    print("2- Listar libros")
    print("3 - SALIR")
    introducido = input()
    print("Has introducido " + introducido)
    opcionInsertada = int(introducido)
    if opcionInsertada == 1:
        print("Introduce los datos del libro")
        nuevoLibro = Libro()
        print("introduce el título")
        nuevoLibro.titulo = input()
        print("introduce las páginas")
        nuevoLibro.paginas = int(input())
        print("introduce el precio")
        nuevoLibro.precio = float(input())
        #Una vez forado el nuevo libro , lo metemos en la lista
        libros.append(nuevoLibro)
        print("LIBRO INSERTADO")
    elif opcionInsertada == 2:
        print("-------Listado de libros--------")
        for l in libros:
            print( "titulo: " + l.titulo + " paginas: " + str(l.paginas) + " precio: " + str(l.precio) )
        print("Fin del listado")
    
print("Fin del programa")