'''
Crear un nuevo proyecto para crear una aplicación de consola que permita
registrar y listar coches

La información de un coche debe contener una marca, un color, año de fabricación,
velocidad máxima y peso
'''
class Coche():
    marca = ""
    color = ""
    anFab = -1
    velMax = -1
    peso = ""
    
coches = []

opcion = -1

while opcion != 3:
    print("Elija una opción\n")
    print("1- Registre un coche\n2- Listado de coches\n3- Salir de la aplicación\n")
    insert = int(input("Opción : "))
    if insert == 1:
        nuevoCoche = Coche()
        print("Indique la marca del coche: ")
        nuevoCoche.marca = input()
        print("Indique el color del coche: ")
        nuevoCoche.color = input()
        print("Indique el año de fabricación del coche: ")
        nuevoCoche.anFab = int(input())
        print("Indique la velocidad máxima del coche: ")
        nuevoCoche.velMax = int(input())
        print("Indique el peso del coche: ")
        nuevoCoche.peso = int(input())
        coches.append(nuevoCoche)
    elif insert == 2:
        for i in coches:
            print("Marca: " + i.marca + " Color: " + i.color + " Año fabricación: " +  str(i.anFab) +
            "  Velocidad máxima: " + str(i.velMax) + " Peso: " + str(i.peso) + "\n")
    elif insert == 3:
        print("Programa finalizado")
        opcion = 3


