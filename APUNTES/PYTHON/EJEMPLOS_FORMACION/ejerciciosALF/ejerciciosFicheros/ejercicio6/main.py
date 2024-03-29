'''
Ejercicio 6
Escribir un programa para gestionar un listín telefónico con los nombres y los 
teléfonos de los clientes de una empresa. El programa deberá incorporar funciones 
para crear el fichero con el listín si no existe, para consultar el teléfono de 
un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un 
cliente. El listín debe estar guardado en el fichero de texto listin.txt donde 
el nombre del cliente y su teléfono deben aparecer separados por comas y cada 
cliente en una línea distinta
'''
from os.path import isfile

run = True

def opcion1():
    nombre = (input("Indica el nombre del cliente : ")).title()        
    archivo = open("listin.txt", "r")
    x = archivo.read() 
    y = x.find(nombre)
    if y != -1:       
        w = y + len(nombre) + 1
        z = w + 9
        print("El tf de " + nombre + " es " + x[w:z] )
    else:
        print("No se encuentra el cliente indicado")
#end opcion1

def opcion2():
    if not isfile("listin.txt"):
        archivo = open("listin.txt", "w")
        nombre = (input("Indica el nombre del cliente : ")).title()
        telefono = input("indica el telefono del cliente : ")
        archivo.write(nombre + ",")
        archivo.write(telefono + "\n")
        archivo.close()
        print("Nuevo cliente registrado")
    else:
        archivo = open("listin.txt", "a")
        nombre = (input("Indica el nombre del cliente : ")).title()
        telefono = input("indica el telefono del cliente : ")
        long = len(telefono)        
        if telefono.isnumeric() and long == 9:
            archivo.write(nombre + ",")
            archivo.write(telefono + "\n")
            archivo.close()
            print("Nuevo cliente registrado")
        else:
            print("El nº de tf indicado no es válido")
            
#end opcion2

def opcion3():
    nombre = input("Indica el nombre del cliente : ").title()
    telefono = input("Indica el nuevo nº de tf : ")
    long = len(telefono)        
    if telefono.isnumeric() and long == 9:
        archivo = open("listin.txt", "r")
        x = archivo.read()            
        y = x.find(nombre)          
        archivo.close()
        if y != -1:                
            w = y + len(nombre) + 1
            z = w + 9
            j = x[w:z]
            archivo = open("listin.txt", "w")                
            archivo.write( x.replace(j, telefono) )
            archivo.close()
            print("Nº de tf modificado correctamente")
        else:
            print("No se encuentra el cliente indicado")           
        
    else:
        print("El nº de tf indicado no es válido")
    
 #end opcion3
 
def runAgain():
    global run
    run_again = input("Deseas realizar otra operación : S/N ").upper()
    if run_again == "S":
        run = True
    else:
        print("Programa finalizado")
        run = False
        
#end runAgain  
    

while run:
    
    print('''
    Elige una opción :
    
        1- Consultar el tf de un cliente
        2- Introducir un nuevo cliente
        3- Modificar el tf de un cliente
        4- Finalizar el programa
        ''')
    
    opcion = input("indicar opción : ")
    
    if opcion.isnumeric():
        
        opcion = int(opcion)
                
        if opcion == 1:
            opcion1()
            runAgain()              
                    
        elif opcion == 2:
            opcion2()
            runAgain()        
                                    
        elif opcion == 3:
            opcion3()
            runAgain()       
            
        elif opcion == 4:
            print("Programa finalizado")
            run = False
    
        else:
            print("Elige una opción válida")
            runAgain()
    
    else:
        print("Elige una opción válida")
        runAgain()
