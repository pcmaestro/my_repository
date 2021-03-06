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

#Variable para comprobar que el jugador elige una longitud de dígitos válida
ComprobarLongitud = True

#Variable para seguir jugando mientras no se adivine el número secreto
jugar = True

#Lista donde se almacenan los números aleatorios generados por el juego
n = []

################### FUNCIONES DEL JUEGO ########################################

#Las variables buffer van almacenando los aciertos del jugador en las posiciones
#del número secreto

#La variable numeroSecreto almacena el número secreto que debe adivinar el jugador

#La variable seleccion es el número introducido por el usuario

def seleccion9digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
        
    if seleccion[3] == numeroSecreto[3]:
        print("Has acertado la posicion 4 del número secreto")
        buffer.append( seleccion[3] )
    
    if seleccion[4] == numeroSecreto[4]:
        print("Has acertado la posicion 5 del número secreto")
        buffer.append( seleccion[4] )
        
    if seleccion[5] == numeroSecreto[5]:
        print("Has acertado la posicion 6 del número secreto")
        buffer.append( seleccion[5] )
    
    if seleccion[6] == numeroSecreto[6]:
        print("Has acertado la posicion 7 del número secreto")
        buffer.append( seleccion[6] )
        
    if seleccion[7] == numeroSecreto[7]:
        print("Has acertado la posicion 8 del número secreto")
        buffer.append( seleccion[7] )
        
    if seleccion[8] == numeroSecreto[8]:
        print("Has acertado la posicion 9 del número secreto")
        buffer.append( seleccion[8] )    
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion9digitos

def seleccion8digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
        
    if seleccion[3] == numeroSecreto[3]:
        print("Has acertado la posicion 4 del número secreto")
        buffer.append( seleccion[3] )
    
    if seleccion[4] == numeroSecreto[4]:
        print("Has acertado la posicion 5 del número secreto")
        buffer.append( seleccion[4] )
        
    if seleccion[5] == numeroSecreto[5]:
        print("Has acertado la posicion 6 del número secreto")
        buffer.append( seleccion[5] )
    
    if seleccion[6] == numeroSecreto[6]:
        print("Has acertado la posicion 7 del número secreto")
        buffer.append( seleccion[6] )
        
    if seleccion[7] == numeroSecreto[7]:
        print("Has acertado la posicion 8 del número secreto")
        buffer.append( seleccion[7] )
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion8digitos

def seleccion7digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
        
    if seleccion[3] == numeroSecreto[3]:
        print("Has acertado la posicion 4 del número secreto")
        buffer.append( seleccion[3] )
    
    if seleccion[4] == numeroSecreto[4]:
        print("Has acertado la posicion 5 del número secreto")
        buffer.append( seleccion[4] )
        
    if seleccion[5] == numeroSecreto[5]:
        print("Has acertado la posicion 6 del número secreto")
        buffer.append( seleccion[5] )
    
    if seleccion[6] == numeroSecreto[6]:
        print("Has acertado la posicion 7 del número secreto")
        buffer.append( seleccion[6] )
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion7digitos

def seleccion6digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
        
    if seleccion[3] == numeroSecreto[3]:
        print("Has acertado la posicion 4 del número secreto")
        buffer.append( seleccion[3] )
    
    if seleccion[4] == numeroSecreto[4]:
        print("Has acertado la posicion 5 del número secreto")
        buffer.append( seleccion[4] )
        
    if seleccion[5] == numeroSecreto[5]:
        print("Has acertado la posicion 6 del número secreto")
        buffer.append( seleccion[5] ) 
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion6digitos

def seleccion5digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
        
    if seleccion[3] == numeroSecreto[3]:
        print("Has acertado la posicion 4 del número secreto")
        buffer.append( seleccion[3] )
    
    if seleccion[4] == numeroSecreto[4]:
        print("Has acertado la posicion 5 del número secreto")
        buffer.append( seleccion[4] )
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion5digitos

def seleccion4digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
        
    if seleccion[3] == numeroSecreto[3]:
        print("Has acertado la posicion 4 del número secreto")
        buffer.append( seleccion[3] )

    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion4digitos

def seleccion3digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion3digitos

def seleccion2digitos():
    
    buffer = []

    if seleccion[0] == numeroSecreto[0]:
        print("Has acertado la posicion 1 del número secreto")
        buffer.append( seleccion[0] )
    
    if seleccion[1] == numeroSecreto[1]:
        print("Has acertado la posicion 2 del número secreto")
        buffer.append( seleccion[1] )
        
    if seleccion[2] == numeroSecreto[2]:
        print("Has acertado la posicion 3 del número secreto")
        buffer.append( seleccion[2] )
    
    if buffer == []:
        print("No has acertado ninguna posición del número secreto")
        
#end seleccion2digitos

######################### INICIO DEL JUEGO #####################################

print("Adivina el número secreto\n")

while ComprobarLongitud:   
        
    longitud = input("\nDime una longitud de 2 a 9 dígitos : ")
    
    if int(longitud) > 1 and int(longitud) < 10:          
    
                     
        for i in range( int(longitud) ):
            n.append( str(randint(0,9)) )
        
        numeroSecreto = "".join(n)       
        
        
        while jugar:   
                
            seleccion = input("\nIndica un número de " + longitud + " digitos : ")   
        
        
            if seleccion == numeroSecreto:
                
                print("Enhorabuena!!!, " + seleccion + " era el número secreto")
                jugar = False       
                ComprobarLongitud = False
            
            else:  
                
                a = len(numeroSecreto)
                b = len(seleccion)
                
                if a == b:
                    
                    if b == 2:                
                        seleccion2digitos()
                    
                    if b == 3:                
                        seleccion3digitos()
                        
                    if b == 4:                
                        seleccion4digitos()
                        
                    if b == 5:                
                        seleccion5digitos()
                        
                    if b == 6:                
                        seleccion6digitos()
                        
                    if b == 7:                
                        seleccion7digitos()
                        
                    if b == 8:                
                        seleccion8digitos()
                        
                    if b == 9:                
                        seleccion9digitos()             
                    
                else:
                    print("\nDebes indicar un número de " + str(a)  + " digitos")
            
    else:
        print("\nDebes indicar una longitud válida entre 2 y 9 dígitos")        
                      
        




    
    

