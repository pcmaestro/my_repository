'''
    MAIN  ***PENDIENTE QUE FUNCIONE EL WHILE***
'''
import time
from listados import avanzar_motos, presentar_motos
from preparar_carrera import preparar_motos

ganado = 0

motos = preparar_motos()

presentar_motos(motos)



reiniciar = True

fin_carrera = False

while reiniciar:
    insertado = input("Introduce el número del ganador : ")
    if ganado == 0:
        apostado = int(input("indica la cantidad que vas a apostar : "))
    else:
        apostado == ganado
    if insertado.isnumeric():
        insertado_int = int(insertado)
        if insertado_int >= 1 and insertado_int < 6:
            while not fin_carrera:
                numero_ganador = avanzar_motos(motos)
                time.sleep(1)
                if numero_ganador != -1:
                    fin_carrera = True
            print("Fin de la carrera, el ganador es el número : " + str(numero_ganador))
            if insertado_int == numero_ganador:                
                    ganado = apostado * int(len(motos))
                    print("Felicidades ,has ganado !! " + str(ganado) + "\n")
                    volver_jugar = input("¿Quieres apostar de nuevo lo que has ganado? S/N : ")
                    if volver_jugar == "S":
                        numero_ganador = -1
                        apostado = ganado
                    else:
                        print("Hasta la próxima")
                        reiniciar = False
            else:
                print("Lo siento, has perdido todo tu dinero")
                reiniciar = False
        else:
            print("Debes elegir un número entro 1 y 5")