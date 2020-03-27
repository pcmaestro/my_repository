##GENERADOR DE OBJETO TIPO GENERATOR ITERABLE
#Estas funciones especiales crean objetos iterables de la clase generator
#Estos iterables son muy efecientes, ya que para recorrerlos o buscar un 
#elemento dentro de ellos,  no se tiene que cargar la colección entera
#con lo cual ahorramos espacio de memoria y recursos de CPU, esto es muy
#util si la colección es gigantesca o infinita

#Estos objetos iterables se pueden recorrer con bucles for y while, pero
#también con el método next()

def generador(numero, limite):
    
    while numero < limite:
        yield numero * 2
        numero += 1    

objeto = generador(1, 10)

print(type(objeto))

print( "Primer elemento " + str( next(objeto) ) )
print( "Segundo elemento " + str( next(objeto) ) )

##GENERADOR DE OBJETO TIPO GENERATOR ITERABLE DE DOS DIMENSIONES

#Con el asterisco en el los parámetros, a cualquier función le indicamos
#que va a recibir un número indeterminado de argumentos

#En este caso , para cada elemento ciudad creado en el objeto generator , la sentencia
#yiled from lo recorrerá letra a letra

def generador2d(*ciudades):
    for ciudad in ciudades:
        yield from ciudad


objeto = generador2d("Madrid", "Barcelona")

print("Primera letra de Madrid es : " + next(objeto) )
print("Segunda letra de Madrid es : " + next(objeto) )
