'''
Ejercicio 2
Escribe un programa que te permita jugar a una versión simplificada del juego 
Master Mind. El juego consistirá en adivinar una cadena de números distintos. 
Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). 
Después el programa debe ir pidiendo que intentes adivinar la cadena de números. 
En cada intento, el programa informará de cuántos números han sido acertados 
(el programa considerará que se ha acertado un número si coincide el valor y la 
posición).
'''
from random import randint

jugar = True
    
print("Adivina el número secreto")
longitud = input("Dime una longitud de 2 a 9 dígitos : ")
                 
n = []
                 
for i in range( int(longitud) ):
    n.append( str(randint(0,9)) )

cadena = "".join(n)


while jugar:   
        
    seleccion = input("Indica un número de " + longitud + " digitos : ")

    if seleccion == cadena:
        
        print("Enhorabuena!!!, " + seleccion + " era el número secreto")
        jugar = False
    
    else:
        
        buffer = []
                
        for i in seleccion:                     
            if i in cadena:
                a = True                

            else:
                a = False
                
        if a == True:
            print("Alguno de los digitos indicados está contenido" + 
                  " al menos una vez en el número secreto")
        
        else:
            print("Ningún digito indicado está incluido" +
                       " en el número secreto, vuelve a intentarlo")







    
    

