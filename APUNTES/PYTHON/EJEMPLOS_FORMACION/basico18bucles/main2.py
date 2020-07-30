'''
Created on 13 mar. 2020

@author: Hp 840 G2
'''
i = 1

while i < 6:
    i += 1
    if i == 3:
        continue # Esta sentencia fuerza al bucle a pasar a la siguiente iteración
                 #En este caso se salta el 3   
    print(i)
print("Ya hemos alcanzado el break")