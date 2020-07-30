#Ejemplo de uso de diccionarios

zapatillas = {
    "color" : "negro",
    "marca" : "nike",
    "precio": 49.99    
}

print(zapatillas)

#Para obtener elementos:

# print(zapatillas[0]) , esto no se puede hacer,  no hay indice

print(zapatillas["color"])

print(zapatillas.get("color"))

#Para recorrer el diccionario, usamos un bucle

#Esto nos devuelve las claves definidas en el diccionario

for e in zapatillas:
    print(e)

#Esto nos devuelve los valores

for e in zapatillas:
    print(e + " : " + str(zapatillas[e]))
 
#Esto nos va mostrando la clave : valor   
for e, v in zapatillas.items():
    print("clave : " + e + "valor : " + str(v) )
    


    