'''
Crear un nuevo proyecto para realizar una aplicación que permita el registro y listado de prendas de ropa.
Dicha prenda será a libre elección, pero deberá tener por lo menos 5 campos
Se debe tomar como referencia el ejemplo basico13modulosSinPaquetes

tareas opcionales :

Incorporar a la aplicación las opciones de registro y listado de clientes
Cada cliente tendrá un nombre, dirección y un email

Incorporar las opciones de poder borrar una prenda y poder borrar un cliente
'''

from menus import *

from listados import *

opcionInsertada = -1

prendas = []

clientes = []

while opcionInsertada != 5:
    opcionInsertada = menuPrincipal()
    if opcionInsertada == 1:
        nuevaPrenda = menuInsertarPrenda()
        prendas.append(nuevaPrenda)
    elif opcionInsertada == 2:
        listadoPrendas(prendas)
    elif opcionInsertada == 3:
        nuevoCliente = menuInsertarCliente()
        clientes.append(nuevoCliente)
    elif opcionInsertada == 4:
        listadoClientes(clientes)
    else:
        print("Fin del programa")
