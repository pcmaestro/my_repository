'''
    PREPARAR CARRERA
'''
import clases

def preparar_motos():
    motos = []
    moto = clases.Moto("Yamaha", "Y1", "negro", "Valentino Rossi", 1, "Italia")
    motos.append(moto)
    moto = clases.Moto("Ducati", "D2", "rojo", "Andrea Dovizioso", 1, "Italia")
    motos.append(moto)
    moto = clases.Moto("Honda", "H3", "naranja", "Marc Marquez", 1, "España")
    motos.append(moto)
    moto = clases.Moto("KTM", "K4", "blanco", "Pol Espargaró", 1, "España")
    motos.append(moto)
    moto = clases.Moto("Suzuki", "S5", "azul", "Dani Martin", 1, "España")
    motos.append(moto)
    return motos
    