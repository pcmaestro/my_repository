'''

Para leer un fichero de internet hay que utilizar la función urlopen 
del módulo urllib.request.

Lo que traemos de la web viene en binario, hay que pasarlo a texto UTF-8 con
el método decode() . El resultado será el HTML publicado en la web

'''
from urllib.request import urlopen


web = urlopen("https://elpais.com/economia/2020-03-19/el-gobierno-asume-que-no-podra-presentar-los-presupuestos-de-2020.html")
contenido = web.read().decode("utf-8")

ruta = "D:/WORKSPACE/LICLIPSE/basico23archivos/archivos/"

file = open(ruta + "ficheroWeb.txt", "w")
file.write(contenido)
file.close()
print("Programa terminado OK")


