'''
MANEJO DE ARCHIVOS

NOTA :  En la carpeta,  renombrar nuevoFichero1.txt a nuevoFichero.txt antes
de ejecturar este programa .  Crear también primero ficheroBorrar.txt , y dejar
ficheroMover.txt en la carpeta archivos
'''
import os

#Creamos un fichero

f = open("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/fichero.txt", "w")

#Escribimos en él

f.write("Esto es todo amigos\n")
f.write("Multiplicate por cero\n")

##OJO, cada vez que abrimos un fichero con el método "w" , machacamos el 
##contenido anterior!!!!

#Cerramos el fichero para que lo pueda usar otra aplicación

f.close()

#Ahora añadimos otro string al final del archivo ( este método no machaca los 
#datos anteriores)

f = open("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/fichero.txt", "a")
f.write("Dinero, Dinero, Dinero.....")
f.close()

#Ahora abrimos el fichero en modo lectura, lo leemos, y copiamos su contenido
#en otro fichero

f = open("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/fichero.txt", "r")
file = f.read()
f.close()

f = open("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/nuevoFichero.txt", "w")
f.write(file)
f.close()

#Este método lee por defecto la primera linea, si le damos el número de línea
#nos devuelve esa línea en concreto

f = open("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/fichero.txt", "r")
file = f.readline()
print(file)
#Si vamos añadiendo mas métodos readline() va leyendo las lineas una a una
file = f.readline()
print(file)
#Le podemos decir al método readline que lea un caracter en concreto, en este caso
#la primera letra ( que ya sería la de la tercera fila)
file = f.readline(1)
print(file)

#El método readlines() convierte el texto en una lista , separando las lineas
#por su salto de línea
f = open("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/fichero.txt", "r")
file = f.readlines()
print(type(file))
print(file)
#Asi podemos ver una fila en concreto
print(file[1])
#Y asi vemos más de una
print("\n")
print(file[1] + "\n" + file[2])
#También podemos mostrar las lineas de la lista creada con readlines() con un
#bucle for
print("\n")
for i in file:
    print(i)
#Ahora usamos el bucle para leer unos caracteres específicos de cada línea
#en este caso , desde el caracter de la posición 13 hasta el final
print("\n")
for linea in file:    
        print(linea[13:])
        
#Habiendo importado el módulo os ,  podemos renombrar, mover y borrar ficheros
#pero antes de hacer nada, SIEMPRE hay que comprobar que el fichero existe en
#con el método os.path.isfile()

fichero = ("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/nuevoFichero.txt")

existeFichero = os.path.isfile(fichero)

#En este caso el print devolverá True , si no existiera el archivo, sería False
print("¿Existe el fichero? : " + str(existeFichero))

#1 renombramos

ficheroNuevoNombre = (
    "D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/nuevoFichero1.txt"
    )
try:
    if existeFichero:
        os.rename( fichero, ficheroNuevoNombre )

except FileExistsError :
    print("El fichero ya existe")


#2 con el mismo método rename , podemos mover el archivo a otro directorio
#con o sin renombrarlo

ruta1 = ("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/ficheroMover.txt")

ruta2 = ("D:/WORKSPACE/LICLIPSE/basico23archivos/archivosMovidos/ficheroMover.txt")

existeFichero = ruta1

try:
    if existeFichero:    
        os.rename(ruta1, ruta2)

except FileNotFoundError:
    print("El fichero ya está movido")

#Con el método os.remove, podemos borrar un fichero

ficheroBorrar = ("D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/ficheroBorrar.txt")

try:
    if ficheroBorrar:
        os.remove(ficheroBorrar)
        print("Fichero borrado")

except FileNotFoundError:
    print("El fichero ya habia sido borrado")



        

        

    



    




