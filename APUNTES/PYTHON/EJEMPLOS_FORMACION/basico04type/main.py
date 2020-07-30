'''
Created on 9 mar. 2020

@author: Hp 840 G2
'''
#Siempre puedo consultar el tipo de dato de una variable usando la función type

variable = "Buenos dias"

tipo = type(variable)

print("Variable : " + variable + " tipo " + str(tipo))

variable2 = 12

tipo2 = type(variable2)

print("Variable : " + str(variable2) + " tipo " + str(tipo2))

variable3 = 0.45

tipo3 = type(variable3)

print("Variable : " + str(variable3) + " tipo " + str(tipo3))

variable4 = ["melon", "fresa"]

tipo4 = type(variable4)

print("Variable : " + str(variable4) + " tipo " + str(tipo4))

##Añadimos un nuevo elemento a nuestra lista

variable4.append("sandia")

print("Variable : " + str(variable4) + " tipo " + str(tipo4))

variable5 = True

tipo5 = type(variable5)

print("Variable : " + str(variable5) + " tipo " + str(tipo5))