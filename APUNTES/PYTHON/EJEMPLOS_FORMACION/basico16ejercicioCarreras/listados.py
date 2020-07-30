'''
    listados
'''
import random

def presentarCaballos(caballos):
    for c in caballos:
        print("numero : " + str(c.numero) + " //nombre : " + c.nombre + " //color : " +
              c.color +  " //posicion : " + str(c.posicion))
        
def avanzar_caballos(caballos):
    numero_ganador = -1
    for c in caballos:
        c.posicion += random.randint(0,5)
        if c.posicion >= 20:
            numero_ganador = c.numero
    print("***************************")
    presentarCaballos(caballos)
    print("---------------------------")
    return numero_ganador