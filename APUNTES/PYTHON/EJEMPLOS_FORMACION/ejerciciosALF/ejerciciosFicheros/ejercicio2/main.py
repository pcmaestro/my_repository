'''
Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número 
introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar 
un mensaje por pantalla informando de ello.
'''
import os

n = int(input("Dame un número entero del 1 al 10 : "))

t = ""

archivo = ("tabla-" + str(n) + ".txt")

ruta = ("D:/WORKSPACE/LICLIPSE/ejerciciosALF/ejerciciosFicheros/ejercicio2/tabla-" 
             + str(n) + ".txt")


def tablaMultiplicar(n):   
    for i in range(11):
        t = (str(n) + " X " + str(i) + " = " + str(n * i) + "\n")        
        f.write(t)        

#end tablaMultiplicar

if not os.path.isfile(ruta):    
    f = open(ruta, "w")
    print("Creado el archivo " + archivo )
    if n > 0 and n < 11:      
        tablaMultiplicar(n)
        f = open(ruta, "r")
        print( f.read() )      
        print("Programa finalizado")        
        f.close()
    else:
        print("El número indicado debe estar entre 0 y 10")
else:
    print("El fichero " + archivo + " ya existe")




   


    