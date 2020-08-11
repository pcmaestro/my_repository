import threading

hilos = 5

inicio_tramo = 1

fin_tramo = inicio_tramo + 19

numeros = []


def enumeracion(inicio, fin):
    rango = (fin - inicio) + 1
    numeros_tramo = (rango//hilos) + 1
    for i in range(inicio, numeros_tramo):
        numeros.append(i)
        inicio += (numeros_tramo) - 1

threads = []


for n in range(hilos):
    for t in threads:
        t = threading.Thread(target= enumeracion, args = [1,100])
        t.start()
        t.join()

print(numeros)




