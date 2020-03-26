'''
    modulo listados
'''
def listar_libros(libros):
    print("Inicio listado de libros")
    for i in libros:
        print("titulo " + i.titulo + " paginas " + i.paginas + " precio " + i.precio)
    print("FIN LISTADO LIBROS")
        