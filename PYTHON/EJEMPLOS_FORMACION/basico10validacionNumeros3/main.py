import re

#Diferentes formas de validar un número

introducido = input("Introduce tu nombre : ")
print("Has introducido " + introducido)

edad = input("Introduce tu edad : ")
#Una vez rocogemos un input del usuario, antes de operar, hay que validar

#Ejemplo de uso de expresiones regulares

expresion = "^\d{1,2}$" 
# RegExp que sólo permite número y luego nada más

resultado = re.match(expresion, edad)
print(resultado)
if resultado:
    print("Gracias por introducir un número")
else:
    print("No has introducido un número")