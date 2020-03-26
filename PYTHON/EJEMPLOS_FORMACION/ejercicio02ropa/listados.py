'''
Created on 10 mar. 2020

@author: Hp 840 G2
'''
def listadoPrendas(prendas):
    print("-----LISTADO DE PRENDAS-----")
    for i in prendas:
        print("Nombre de la prenda : " + i.nombre + " //Talla : " + i.talla + " //Color : " + i.color + " //Tejido : " + i.tejido + " //Adulto/Niño : " + i.adultoNino + " //Hombre/Mujer : " + i.sexo)
    print("-----FIN DEL LISTADO-----")
    
def listadoClientes(clientes):
    print("------LISTADO DE CLIENTES------")
    for j in clientes:
        print("Nombre : " + j.nombreCompleto + " //Dirección : " + j.direccion + " //E-mail : " + j.email)