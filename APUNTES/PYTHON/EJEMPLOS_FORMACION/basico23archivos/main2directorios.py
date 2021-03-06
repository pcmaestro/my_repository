'''
CREACION, MODIFICACION Y BORRADO DE DIRECTORIOS

Para trabajar con directorios también se utilizan funciones del módulo os.

os.mkdir(ruta) : Crea un nuevo directorio en la ruta

os.chdir(ruta) : Cambia el directorio actual al indicado por la ruta

os.getcwd() : Devuelve una cadena con la ruta del directorio actual.

os.rmdir(ruta) : Borra el directorio de la ruta ruta, siempre y cuando esté vacío.
'''

import os

nuevoDirectorio = "prueba1"

ruta = "D:/WORKSPACE/LICLIPSE/basico23archivos/archivos"

rutaCompleta = ruta + "/" + nuevoDirectorio

if rutaCompleta:
    os.rmdir(rutaCompleta)
    os.mkdir(rutaCompleta)
print("Programa terminado")

#Esto devuelve el directorio actual donde se ejecuta el programa python
print("Nuestro programa se está ejecutando en el directorio :" +  "\n" +
      os.getcwd() )




