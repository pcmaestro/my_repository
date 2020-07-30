from preparar_carrera import preparar_caballos
from listados import presentarCaballos, avanzar_caballos
import time

#Obtengo los caballos que me de el return de la función preparar_caballos()
caballos = preparar_caballos()

#Dichos caballos se los doy a la función presentar_caballos() para que los muestre en pantalla

presentarCaballos(caballos)

print("Introduce el número del ganador : ")
insertado = input()
insertado_int = int(insertado)

fin_carrera = False

while not fin_carrera :
    numero_ganador = avanzar_caballos(caballos)
    time.sleep(1)
    if numero_ganador != -1:
        fin_carrera = True # Esto finaliza el while y los caballos dejan de correr
print("Fin de la carrera")
if insertado_int == numero_ganador:
    print("Felicidades ,has ganado !!")
else:
    print("Lo siento, has perdido")
     
    