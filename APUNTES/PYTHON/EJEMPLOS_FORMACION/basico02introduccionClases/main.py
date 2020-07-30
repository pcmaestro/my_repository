'''
Created on 9 mar. 2020

@author: Hp 840 G2
'''
class Coche():
    marca = "no asignado"
    color = "no asignado"
    anio = -1
    
    def pitar(self):
        print("bip")
    
coche1 = Coche() # Creamos una variable que tenga todo lo definido en la clase coche

coche2 = Coche()

coche1.marca = "Ferrari"

print("marca de coche1 " + coche1.marca)

print("marca de coche2 " + coche2.marca)

coche1.pitar()


