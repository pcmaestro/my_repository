'''
    LISTADOS
'''
import random

def presentar_motos(motos):
    for moto in motos:
        print("MARCA : " + moto.marca + " MODELO : " + moto.modelo + " COLOR : " + moto.color +
              " PILOTO : " + moto.piloto + " NUMERO : " + str(moto.numero) +
              " PAIS : " + moto.pais + " POSICION : " + str(moto.posicion))
        
def avanzar_motos(motos):
    numero_ganador = -1
    for moto in motos:
        moto.posicion += random.randint(0,5)
        if moto.posicion >= 20:
            numero_ganador = moto.numero
    print("***************************")
    presentar_motos(motos)
    print("---------------------------")
    return numero_ganador

