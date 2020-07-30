import time
import random

input("Pulsa enter cuando estés listo")
print("preparate.........")
time.sleep(1 + random.random()) # random() genera aleatorios entre 0.0 y 1
tini = time.time() # En esta variable alamacenamos la fecha y hora actual en forma
                   # de un número entero contando milisegundos desde 01/01/1970

input("Pular enter de nuevo")
tfin = time.time()

tiempo_tardado = tfin - tini

print("Tu tiempo de reacción es de " + str(tiempo_tardado) )