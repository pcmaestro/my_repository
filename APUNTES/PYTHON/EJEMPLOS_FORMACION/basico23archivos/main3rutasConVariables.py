'''
Created on 20 mar. 2020

@author: hipercor
'''
nuevoArchivo = "ficheroPrueba2.txt"

ruta = "D:/WORKSPACE/LICLIPSE/basico23archivos/archivos"

rutaCompleta1 = ruta + "/" + nuevoArchivo
f = open(rutaCompleta1, "w")
f.write("Esto es una prueba")
f.close()
print("Programa finalizado")



