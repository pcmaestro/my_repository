'''
Ejercicio 4
Escribir un programa que acceda a un fichero de internet mediante su url y 
muestre por pantalla el número de palabras que contiene.
'''
from urllib.request import urlopen


web = urlopen("https://github.com/pcmaestro/my_repository/blob/master/SQL/INSERT.sql")
contenido = web.read().decode("utf-8")

lista = contenido.split()
print("En la web hay " + str(len(lista)) + " palabras")
print("Programa finalizado")