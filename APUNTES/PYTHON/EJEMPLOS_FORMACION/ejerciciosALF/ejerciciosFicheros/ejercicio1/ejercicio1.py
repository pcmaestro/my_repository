'''
Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
donde n es el número introducido.
'''
import os

n = int(input("Dame un número entero del 1 al 10 : "))
t = ""

def tablaMultiplicar(n):    
    for i in range(11):
        t = (str(n) + " X " + str(i) + " = " + str(n * i) + "\n")
        f.write(t)

#end tablaMultiplicar

f = open("D:/WORKSPACE/LICLIPSE/ejerciciosALF/ejerciciosFicheros/ejercicio1/tabla-" 
+ str(n) + ".txt", "w")  

if n > 0 and n < 11:    
    tablaMultiplicar(n)
    print("Programa finalizado")
else:
    print("El número indicado debe estar entre 0 y 10")      

f.close()
    