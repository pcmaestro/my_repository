'''
Ejercicio 3
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden 
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos 
últimas tiene que decir que riman un poco y si no, que no riman.
'''
palabra1 = input("Dime una palabra : ")

palabra2 = input("\nDime otra palabra : ")

#Slice de los dos últimos caracteres de ambas palabras
ult2pal1 = palabra1[-2:]
ult2pal2 = palabra2[-2:]

#Slice de los tres últimos caracteres de ambas palabras
ult3pal1 = palabra1[-3:]
ult3pal2 = palabra2[-3:]

if ult3pal1[0] == ult3pal2[0] and ult3pal1[1] == ult3pal2[1] and ult3pal1[2] == ult3pal2[2]:
    print("\nLas palabras riman")

elif ult2pal1[0] == ult2pal2[0] and ult2pal1[1] == ult2pal2[1]:
    print("\nLas palabras riman un poco")   

else:
    print("\nLas palabras no riman")
    
