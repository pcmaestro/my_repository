'''
Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla 
la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por 
pantalla informando de ello
'''
import os

n = int(input("Dame un número entero del 1 al 10 : "))

m = int(input("Dame otro número entero del 1 al 10 : "))

t = ""

archivo = ("tabla-" + str(n) + ".txt")

ruta = ("D:/WORKSPACE/LICLIPSE/ejerciciosALF/ejerciciosFicheros/ejercicio3/tabla-" 
             + str(n) + ".txt")


def tablaMultiplicar(n):   
    for i in range(11):
        t = (str(n) + " X " + str(i) + " = " + str(n * i) + "\n")        
        f.write(t)        

#end tablaMultiplicar

if not os.path.isfile(ruta):    
    f = open(ruta, "w")
    print("El archivo no exsitia, se ha creado el archivo " + archivo )
    if n > 0 and n < 11:      
        tablaMultiplicar(n)
        f = open(ruta, "r")        
        x = f.read()
        #Localizamos la posición en el string de la cadena deseada
        y = x.find(str(n) + " X " + str(m) + " = " + str(n * m) + "\n")
        #Preparamos al cantidad de caracteres a extraer con el slice
        z = y + 11
        print(x[y:z])
        print("Programa finalizado")        
        f.close()
    else:
        print("El número indicado debe estar entre 0 y 10")
else:
    print("El fichero " + archivo + " ya existe")
    f = open(ruta, "r")        
    x = f.read()
    #Localizamos la posición en el string de la cadena deseada
    y = x.find(str(n) + " X " + str(m) + " = " + str(n * m) + "\n")
    #Preparamos al cantidad de caracteres a extraer con el slice
    z = y + 11
    print(x[y:z])
    print("Programa finalizado")        
    f.close()




   


    