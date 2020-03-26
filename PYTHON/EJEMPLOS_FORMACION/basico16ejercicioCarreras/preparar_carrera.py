'''
    preparar_carrera
'''

import clases

def preparar_caballos():
    caballos = []
    #En vez de ir caballo a caballo , usamos un constructor. Si la clase tiene el constructor
    #definido , es obligatorio usarlo para rellenar las propiedades de los objetos
    c = clases.Caballo("Rapido", "blanco", 1)
    caballos.append(c)   
    c = clases.Caballo("Flecha", "Negro", 2)
    caballos.append(c)
    c = clases.Caballo("Viento", "Marron", 3)
    caballos.append(c)
    c = clases.Caballo("Luna", "Gris", 4)
    caballos.append(c)
    return caballos
                  