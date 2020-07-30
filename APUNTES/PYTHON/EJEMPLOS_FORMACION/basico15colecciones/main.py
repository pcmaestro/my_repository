#Ejemplo de uso de listas

lista_vacia = []

lista_nombres = ["Jose", "Ana", "Sofia"]

print(lista_vacia)

print(lista_nombres)

segundo_elemento = lista_nombres[1]

print("Segundo elemento : " + segundo_elemento)

ultimo_elemento = lista_nombres[-1]

print("Ultimo elemento : " + ultimo_elemento)

#Para traer los elementos desde la posición 1 del índice hasta el final
print("Parte de la lista" + str(lista_nombres[1:]))

#Para sacar el tamaño de la lista
print("tamaño lista_nombres : " + str(len(lista_nombres)))

#Para eliminar elementos

print("lista hasta ahora")
print(lista_nombres)
#lista_nombres.remove("Ana")

#Lo mismo, pero por indice
##lista_nombres.remove(lista_nombres[1])

#Y ahora con pop()
#lista_nombres.pop(1)

#Y ahora con del
del lista_nombres[1]

print("lista después de borrar")
print(lista_nombres)

#Unir listas

nombres2 = ["Adrian", "Gema"]

lista3 = lista_nombres + nombres2

print("lista_nombres + nombres2" + str(lista3))